{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled63.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPOs04VO3L4APDXJB5Unj1x",
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
        "<a href=\"https://colab.research.google.com/github/diegowalhernandes/exercicios-python/blob/main/Desafio023\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M-FG7OhNGqcM",
        "outputId": "9f7b1053-f9aa-4b61-e0de-4146e0ca32a1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Informe um número: 1989\n",
            "Analisando o número 1989\n",
            "Unidade: 9\n",
            "Dezena: 8\n",
            "Centena: 9\n",
            "Milhar: 1\n"
          ]
        }
      ],
      "source": [
        "'''Desafio 023\n",
        "Faça um programa que leia um número de 0 a 9999\n",
        "e mostre na tela cada um dos digitos separados.\n",
        "Ex:\n",
        "Digite um número: 1834\n",
        "unidade: 4 dezena: 3 centena: 8 milhar: 1'''\n",
        "\n",
        "num = int(input('Informe um número: '))\n",
        "u = num // 1 % 10\n",
        "d = num // 10 % 10\n",
        "c = num // 100 % 10\n",
        "m = num // 1000 % 10\n",
        "print(f'Analisando o número {num}')\n",
        "print(f'Unidade: {u}')\n",
        "print(f'Dezena: {d}')\n",
        "print(f'Centena: {c}')\n",
        "print(f'Milhar: {m}')"
      ]
    }
  ]
}
