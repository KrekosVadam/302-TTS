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
        
        self.dataset_path = "/project/project/voices/dataset"
        self.transcript_file = "./project/voices/dataset/metadata.csv"
        self.model_files_path = "/project/project/voices/training-resources/epoch=4641-step=3104302.ckpt"  # Local path to model file
        self.config_files_path = "/project/project/voices/training-resources"  # Local path to config file
        
        self.output_path = "/project/piper"
        self.output_dir = self.output_path+"/"+"test_model"
        
        # pretrained model paths
        self.pretrained_model_path = "/project/project/voices/en_US-ryan-high.onnx"
        self.pretrained_config_path = "/project/project/voices/en_US-ryan-high.onnx.json"

        # Set up piper_train
        self.run_command("sh ./piper/src/python/build_monotonic_align.sh")

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
        
        if not os.path.exists(self.transcript_file):
            raise FileNotFoundError(f"Metadata file not found: {self.transcript_file}")
    
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)        
            
        os.chdir(os.path.join('piper', 'src', 'python'))
            
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
        print("Choose an action:")
        print("1. Finetune")
        print("2. Continue Training")
    
        # Ask for user input and ensure it's either '1' or '2'
        action = input("Enter 1 or 2: ").strip()
        
        if action == "2":
            if os.path.exists(self.dataset_path+"/test_model.ckpt"):
                ft_command = f'--resume_from_checkpoint "{output_dir}, last.ckpt" '
                print(f"Continuing {model_name}'s training at: {output_dir}, last.ckpt")
            else:
                raise Exception("Training cannot be continued as there is no checkpoint to continue at.")    
        if action == "1":
            if os.path.exists(self.dataset_path+"/test_model.ckp"):
                raise Exception("Oh no! You have already trained this model before, you cannot choose this option since your progress will be lost, and then your previous time will not count. Please select the option to continue a training.")
            else:
                ft_command = "--resume_from_checkpoint '{checkpoint_path}' ".format(checkpoint_path=self.model_files_path)
                
        batch_size = 12
        validation_split = 0.01
        quality = "medium"
        checkpoint_epochs = 5
        log_every_n_steps = 1000
        max_epochs = 10000
        
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
                            
    def run(self):
        self.preprocess()
        self.train()
        print("Done!")