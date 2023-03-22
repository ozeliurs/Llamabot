import subprocess


class LLAMA:
    def __init__(self):
        self.params = {
            'model': 'llama.cpp/models/7B/ggml-model-q4_0.bin',
            'tokens': 512,
            'repeat_penalty': 1.0,
            'temperature': 0.7,
            'top_k': 10000,
        }

    def exec(self, prompt: str) -> str:
        cmd = f"llama.cpp/main -m {self.params['model']} -p \"{prompt}\" -n {self.params['tokens']} --repeat_penalty {self.params['repeat_penalty']} -t {self.params['temperature']} -k {self.params['top_k']}"
        return subprocess.check_output(cmd, shell=True).decode('utf-8')
