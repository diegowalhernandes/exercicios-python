{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Desafio016.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOwOMSEAcBFm+sYg6Pcn5aq",
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
        "<a href=\"https://colab.research.google.com/github/diegowalhernandes/exercicios-python/blob/main/Desafio016.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_nivUgvo8i3G",
        "outputId": "7f07fb52-030a-4107-df0e-5050bb313ff0"
      },
      "source": [
        "import math\n",
        "print('''===Desafio 016===\n",
        "Crie um programa que leia um numero Real\n",
        "qualquer pelo teclado e mostre n atela a sua porção \n",
        "inteira.''')\n",
        "print('=-'*15)\n",
        "num = float(input('Digite um número: '))\n",
        "print(f'O número digitado foi {num} e sua porção inteira é {math.trunc(num)}')"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "===Desafio 016===\n",
            "Crie um programa que leia um numero Real\n",
            "qualquer pelo teclado e mostre n atela a sua porção \n",
            "inteira.\n",
            "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n",
            "Digite um número: 4.542\n",
            "O número digitado foi 4.542 e sua porção imteira é 4\n"
          ]
        }
      ]
    }
  ]
}
