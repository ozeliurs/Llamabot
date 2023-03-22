FROM debian:stretch-slim

# Download LLAMA
RUN git clone https://github.com/ggerganov/llama.cpp



# Compile LLAMA
RUN cd llama.cpp && \
    make && \
    cd ..

# Install python dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install torch numpy sentencepiece && \
    pip3 install -r requirements.txt

#
RUN python3 convert-pth-to-ggml.py models/7B/ 1