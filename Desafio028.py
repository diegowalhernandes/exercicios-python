{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Desafio028.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPI/ppwkKMDgqUNz+5xd4aA",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/diegowalhernandes/exercicios-python/blob/main/Desafio028.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kcufodc7ydoG",
        "outputId": "24650868-2ca5-4727-e52a-07b09eca360b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n",
            "Pensei em um número entre 0 e 5, Tente adivinhar...\n",
            "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n",
            "Em que número eu pensei? 4\n",
            "PARABÉNS! Você acertou!\n"
          ]
        }
      ],
      "source": [
        "'''Jogo da adivinhação\n",
        "\n",
        "Escreva um programa que faça o computador \"pensar\" em\n",
        "um número inteiro entre 0 e 5 e peça para o usuário\n",
        "tentar descobrir qual foi o número escolhido pelo \n",
        "computador.\n",
        "\n",
        "O programa deverá escrever na tela se o \n",
        "usuário venceu ou perdeu'''\n",
        "\n",
        "from random import randint\n",
        "computador = randint(0,5)\n",
        "print('-='*20)\n",
        "print('Pensei em um número entre 0 e 5, Tente adivinhar...')\n",
        "print('-='*20)\n",
        "jogador = int(input('Em que número eu pensei? '))\n",
        "if jogador == computador:\n",
        "  print('PARABÉNS! Você acertou!')\n",
        "else:\n",
        "  print(f'Ganhei eu pensei no número {computador}')\n",
        "\n"
      ]
    }
  ]
}