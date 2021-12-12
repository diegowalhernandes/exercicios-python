{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Desafio017a.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOI5i3jTEAJGm/tZKkINisG",
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
        "<a href=\"https://colab.research.google.com/github/diegowalhernandes/exercicios-python/blob/main/Desafio017a.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gvI9xGa7-Jzn",
        "outputId": "d0637531-4def-4863-a151-305ddc45d77a"
      },
      "source": [
        "print('''===Desafio 017===\n",
        "Faça um programa que leia o \n",
        "comprimento do cateto oposto e do \n",
        "cateto adjacente de um triângulo\n",
        "retângulo, calcule e mostre o compromento \n",
        "da hipotenusa.''')\n",
        "print('=-'*15)\n",
        "\n",
        "co = float(input('Comprimento do cateto oposto: '))\n",
        "ca = float(input('Comprimento do cateto adjacente: '))\n",
        "hi = (co ** 2 + ca ** 2) ** (1/2)\n",
        "print(f'A hipotenusa vai medir {hi:.2f}')"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "===Desafio 017===\n",
            "Faça um programa que leia o \n",
            "comprimento do cateto oposto e do \n",
            "cateto adjacente de um triângulo\n",
            "retângulo, calcule e mostre o compromento \n",
            "da hipotenusa.\n",
            "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n",
            "Comprimento do cateto oposto: 2\n",
            "Comprimento do cateto adjacente: 2.5\n",
            "A hipotenusa vai medir 3.20\n"
          ]
        }
      ]
    }
  ]
}
