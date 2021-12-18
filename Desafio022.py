{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Desafio22.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMypvI9AfKy0oZ5ESZqOFE2",
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
        "<a href=\"https://colab.research.google.com/github/diegowalhernandes/exercicios-python/blob/main/Desafio22.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZAOpTlEJCKuG",
        "outputId": "46e10ae2-2507-44f9-9193-86f0350d4e3e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite seu nome completo: Joao da silva\n",
            "Analisando nome...\n",
            "Seu nome em maiusculas é JOAO DA SILVA\n",
            "Seu nome em minusculas é joao da silva\n",
            "Seu nome tem ao todo 11 letras\n",
            "Seu primeiro nome é 4\n"
          ]
        }
      ],
      "source": [
        "'''Exercício Python #22\n",
        "Analisador de Textos\n",
        "Crie um programa que leia o nome completo de uma\n",
        "pessoa e mostre:\n",
        "1 O nome com todas as letras maiúsculas\n",
        "2 O nome com todas minúsculas.\n",
        "3 Quantas letras ao todo (sem considerar espaços)\n",
        "4 Quantas letras tem o primeiro nome'''\n",
        "\n",
        "nome = str(input(\"Digite seu nome completo: \")).strip()\n",
        "print(\"Analisando nome...\")\n",
        "print(f\"Seu nome em maiusculas é {nome.upper()}\")\n",
        "print(f\"Seu nome em minusculas é {nome.lower()}\")\n",
        "print(f\"Seu nome tem ao todo {(len(nome)-nome.count(' '))} letras\")\n",
        "print(f\"Seu primeiro nome é {nome.find(' ')}\")"
      ]
    }
  ]
}
