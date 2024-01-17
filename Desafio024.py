{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Desafio024.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNuB5PoKbvnkiGYCVYf2TJ5",
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
        "<a href=\"https://colab.research.google.com/github/diegowalhernandes/exercicios-python/blob/main/Desafio024.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EeHlFE95MlfW",
        "outputId": "e92a7ead-cc01-4948-b601-93e1c1524e30"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Em que cidade você nasceu? Santos\n",
            "True\n"
          ]
        }
      ],
      "source": [
        "'''Desafio024\n",
        "Crie um progrma que lleia p nome de uma cidade\n",
        "se ela começa ou não com o nome \"SANTO\".'''\n",
        "\n",
        "cidade = str(input('Em que cidade você nasceu? ')).strip()\n",
        "print(cidade[:5].upper() == 'SANTO')\n"
      ]
    }
  ]
}