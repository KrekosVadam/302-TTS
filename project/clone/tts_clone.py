import os
import subprocess

from piper.voice import PiperVoice

class TTSClone:
    
    def __init__(self): 
        # model name
        # dataset format
        # single speaker
        # sample rate
        # resample
        
        self.dataset_path = "/project/project/voices/jadon-voice-samples"
        self.model_files_path = "/project/project/voices/training-resources/epoch=4641-step=3104302.ckpt"  # Local path to model file
        
        self.output_path = "/project/voice_model"
        self.output_logs = self.output_path+"/"+"lightning_logs"

        self.export_voice_path = "/project/project/voices/"
        self.ckpt_path = "/project/voice_model/lightning_logs/version_0/checkpoints/*.ckpt"
        self.model_name = "custom"

        # Set up piper_train
        self.run_command("bash ./piper/src/python/build_monotonic_align.sh")

    def run_command(self, command):
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            raise Exception("Command failed: " + command)
    
    def preprocess(self):    
        print("Preprocessing dataset...")
        language = "en-US"  # Set your language
        dataset_format = "ljspeech"  # Set your dataset format
        sample_rate = "22050"  # Set your sample rate
        single_speaker = True  # Set if this is a single speaker dataset
    
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path) 

        if not os.path.exists(self.output_logs):
            os.makedirs(self.output_logs)    
            
        # Build preprocess command
        preprocess_command = (
            "python -m piper_train.preprocess " +
            "--language '" + language + "' " +
            "--input-dir " + self.dataset_path + " " +
            "--output-dir " + self.output_path + " " +
            "--dataset-format " + dataset_format + " " +
            "--sample-rate " + sample_rate + " " +
            ("--single-speaker" if single_speaker else "")
        )
        
        self.run_command(preprocess_command)
        
    def list_output_directory(self):
        print("Files in output directory:")
        for file_name in os.listdir(self.output_path):
            print(file_name)
        
    def train(self): 
        print("Training...")

        if os.path.exists(self.dataset_path+"/test_model.ckp"):
            raise Exception("Oh no! You have already trained this model before, you cannot choose this option since your progress will be lost, and then your previous time will not count. Please select the option to continue a training.")
        else:
            ft_command = "--resume_from_checkpoint '{checkpoint_path}' ".format(checkpoint_path=self.model_files_path)
                
        batch_size = 1
        validation_split = 0.01
        quality = "medium"
        checkpoint_epochs = 1
        log_every_n_steps = 1
        max_epochs = 4643
        
        train_command = (
            "python -m piper_train " +
            "--dataset-dir '{output_path}' ".format(output_path=self.output_path) +
            "--accelerator 'cpu' " +
            "--devices 1 " +
            "--batch-size {batch_size} ".format(batch_size=batch_size) +
            "--validation-split {validation_split} ".format(validation_split=validation_split) +
            "--num-test-examples 2 " +
            "--quality {quality} ".format(quality=quality) +
            "--checkpoint-epochs {checkpoint_epochs} ".format(checkpoint_epochs=checkpoint_epochs) +
            "--log_every_n_steps {log_every_n_steps} ".format(log_every_n_steps=log_every_n_steps) +
            "--max_epochs {max_epochs} ".format(max_epochs=max_epochs) +
            "{ft_command} ".format(ft_command=ft_command) +
            "--precision 32"
        )
        
        self.run_command(train_command)

    def export(self):
        print("Exporting model...")
        export_command = (
            "python -m piper_train.export_onnx " +
            "{ckpt_path} ".format(ckpt_path=self.ckpt_path)  +
            "{export_voice_path}".format(export_voice_path=self.export_voice_path+self.model_name+".onnx")
        )
        os.rename("/project/voice_model/config.json", "/project/project/voices/{model_name}.onnx.json".format(model_name=self.model_name))

        self.run_command(export_command)
                            
    def run(self):
        os.chdir(os.path.join('piper', 'src', 'python'))
        self.preprocess()
        self.train()
        self.export()
        os.chdir("/project")
        print("Done!")