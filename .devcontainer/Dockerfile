FROM python

ENV PYTHONPATH=.
RUN apt update -y && apt install zsh git curl -y
RUN pip3 install --upgrade pip poetry
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"