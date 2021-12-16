{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Desafio024.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNto4lZDb/y7sRwprSy05nC",
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
        "<a href=\"https://colab.research.google.com/github/diegowalhernandes/exercicios-python/blob/main/Desafio025.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EeHlFE95MlfW",
        "outputId": "a93d6e91-07cf-4a9b-93e9-47c4697c1d8d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Qual é seu nome completo? Silva Sauro\n",
            "Seu nome tem Silva? True\n"
          ]
        }
      ],
      "source": [
        "'''Desafio025\n",
        "Crie um programa que leia o nome de uma pessoa e \n",
        "diga se ela tem \"Silva\" no nome.'''\n",
        "\n",
        "nome = str(input('Qual é seu nome completo? ')).strip().upper()\n",
        "res = 'SILVA' in nome\n",
        "print(f'Seu nome tem Silva? {res}')\n"
      ]
    }
  ]
}