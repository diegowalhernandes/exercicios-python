{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Desafio026.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNKV7MlTvh8fCbMLan4i4Xu",
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
        "<a href=\"https://colab.research.google.com/github/diegowalhernandes/exercicios-python/blob/main/Desafio026.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nl-_bHqwqpRZ",
        "outputId": "70c03f84-39fd-4de5-c98d-81b8a16ad1b4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite uma frase: Arara Azul\n",
            "A letra A aparece 4 vezes na frase.\n",
            "A primeira letra A apareceu na posição 1\n",
            "A última letra A apareceu na posição 7\n"
          ]
        }
      ],
      "source": [
        "'''Desafio026\n",
        "\n",
        "Faça um programa que leia uma frase pelo teclado e mostre:\n",
        "Quantas vezes aparece a letra \"A\".\n",
        "Em que posição ela aparece a primeira vez.\n",
        "Em que posição ela aparece a última vez.'''\n",
        "\n",
        "frase = str(input('Digite uma frase: ')).upper().strip()\n",
        "print(f'A letra A aparece {(frase.count(\"A\"))} vezes na frase.')\n",
        "print(f'A primeira letra A apareceu na posição {(frase.find(\"A\")+1)}')\n",
        "print(f'A última letra A apareceu na posição {(frase.rfind(\"A\")+1)}')"
      ]
    }
  ]
}