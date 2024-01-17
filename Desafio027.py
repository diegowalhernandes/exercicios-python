{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Desafio.027",
      "provenance": [],
      "authorship_tag": "ABX9TyMyJmHx1+aGVJ0Hak0tZIqA",
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
        "<a href=\"https://colab.research.google.com/github/diegowalhernandes/exercicios-python/blob/main/Desafio027.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Glw386cj26TP",
        "outputId": "75f4f5da-b501-42cb-c2da-02223ef1ee61"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite seu nome completo: Pedro Alvarez Cabral\n",
            "Muito prazer em te conhecer!\n",
            "Seu primeiro nome é Pedro\n",
            "Seu último nome é Cabral\n"
          ]
        }
      ],
      "source": [
        "'''Desafio027\n",
        "Faça um programa que leia o nome completo de uma pessoa,\n",
        "mostrando em seguida o primeiro e o último nome\n",
        "separadamente.\n",
        "Ex: Ana Maria de Souza\n",
        "priemiro = Ana\n",
        "último = Souza'''\n",
        "\n",
        "n = str(input('Digite seu nome completo: ')).strip()\n",
        "nome = n.split()\n",
        "print('Muito prazer em te conhecer!')\n",
        "print(f'Seu primeiro nome é {(nome[0])}')\n",
        "print(f'Seu último nome é {(nome[len(nome)-1])}')\n"
      ]
    }
  ]
}