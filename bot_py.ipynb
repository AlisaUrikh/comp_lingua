{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMr3TkwthmZiuDLoBcVI/B6",
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
        "<a href=\"https://colab.research.google.com/github/AlisaUrikh/comp_lingua/blob/main/bot_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7jCBQpBAHBPk",
        "outputId": "47bc44ca-303c-4d95-9d8f-d17c8953ebec"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: nltk in /usr/local/lib/python3.11/dist-packages (3.9.1)\n",
            "Requirement already satisfied: gensim in /usr/local/lib/python3.11/dist-packages (4.3.3)\n",
            "Requirement already satisfied: scikit-learn in /usr/local/lib/python3.11/dist-packages (1.6.1)\n",
            "Collecting aiogram\n",
            "  Downloading aiogram-3.18.0-py3-none-any.whl.metadata (7.6 kB)\n",
            "Requirement already satisfied: click in /usr/local/lib/python3.11/dist-packages (from nltk) (8.1.8)\n",
            "Requirement already satisfied: joblib in /usr/local/lib/python3.11/dist-packages (from nltk) (1.4.2)\n",
            "Requirement already satisfied: regex>=2021.8.3 in /usr/local/lib/python3.11/dist-packages (from nltk) (2024.11.6)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.11/dist-packages (from nltk) (4.67.1)\n",
            "Requirement already satisfied: numpy<2.0,>=1.18.5 in /usr/local/lib/python3.11/dist-packages (from gensim) (1.26.4)\n",
            "Requirement already satisfied: scipy<1.14.0,>=1.7.0 in /usr/local/lib/python3.11/dist-packages (from gensim) (1.13.1)\n",
            "Requirement already satisfied: smart-open>=1.8.1 in /usr/local/lib/python3.11/dist-packages (from gensim) (7.1.0)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn) (3.5.0)\n",
            "Collecting aiofiles<24.2,>=23.2.1 (from aiogram)\n",
            "  Downloading aiofiles-24.1.0-py3-none-any.whl.metadata (10 kB)\n",
            "Requirement already satisfied: aiohttp<3.12,>=3.9.0 in /usr/local/lib/python3.11/dist-packages (from aiogram) (3.11.12)\n",
            "Requirement already satisfied: certifi>=2023.7.22 in /usr/local/lib/python3.11/dist-packages (from aiogram) (2025.1.31)\n",
            "Collecting magic-filter<1.1,>=1.0.12 (from aiogram)\n",
            "  Downloading magic_filter-1.0.12-py3-none-any.whl.metadata (1.5 kB)\n",
            "Requirement already satisfied: pydantic<2.11,>=2.4.1 in /usr/local/lib/python3.11/dist-packages (from aiogram) (2.10.6)\n",
            "Requirement already satisfied: typing-extensions<=5.0,>=4.7.0 in /usr/local/lib/python3.11/dist-packages (from aiogram) (4.12.2)\n",
            "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<3.12,>=3.9.0->aiogram) (2.4.6)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.11/dist-packages (from aiohttp<3.12,>=3.9.0->aiogram) (1.3.2)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<3.12,>=3.9.0->aiogram) (25.1.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.11/dist-packages (from aiohttp<3.12,>=3.9.0->aiogram) (1.5.0)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.11/dist-packages (from aiohttp<3.12,>=3.9.0->aiogram) (6.1.0)\n",
            "Requirement already satisfied: propcache>=0.2.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<3.12,>=3.9.0->aiogram) (0.3.0)\n",
            "Requirement already satisfied: yarl<2.0,>=1.17.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<3.12,>=3.9.0->aiogram) (1.18.3)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<2.11,>=2.4.1->aiogram) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.11/dist-packages (from pydantic<2.11,>=2.4.1->aiogram) (2.27.2)\n",
            "Requirement already satisfied: wrapt in /usr/local/lib/python3.11/dist-packages (from smart-open>=1.8.1->gensim) (1.17.2)\n",
            "Requirement already satisfied: idna>=2.0 in /usr/local/lib/python3.11/dist-packages (from yarl<2.0,>=1.17.0->aiohttp<3.12,>=3.9.0->aiogram) (3.10)\n",
            "Downloading aiogram-3.18.0-py3-none-any.whl (612 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m612.8/612.8 kB\u001b[0m \u001b[31m10.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading aiofiles-24.1.0-py3-none-any.whl (15 kB)\n",
            "Downloading magic_filter-1.0.12-py3-none-any.whl (11 kB)\n",
            "Installing collected packages: magic-filter, aiofiles, aiogram\n",
            "Successfully installed aiofiles-24.1.0 aiogram-3.18.0 magic-filter-1.0.12\n"
          ]
        }
      ],
      "source": [
        "!pip install nltk gensim scikit-learn aiogram"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install spacy\n",
        "!python -m spacy download ru_core_news_sm"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YvAQpYZSHE8M",
        "outputId": "0e8f7b5c-88ee-4923-fe93-ba26dc6caee1"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: spacy in /usr/local/lib/python3.11/dist-packages (3.7.5)\n",
            "Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.11 in /usr/local/lib/python3.11/dist-packages (from spacy) (3.0.12)\n",
            "Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (1.0.5)\n",
            "Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (1.0.12)\n",
            "Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /usr/local/lib/python3.11/dist-packages (from spacy) (2.0.11)\n",
            "Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /usr/local/lib/python3.11/dist-packages (from spacy) (3.0.9)\n",
            "Requirement already satisfied: thinc<8.3.0,>=8.2.2 in /usr/local/lib/python3.11/dist-packages (from spacy) (8.2.5)\n",
            "Requirement already satisfied: wasabi<1.2.0,>=0.9.1 in /usr/local/lib/python3.11/dist-packages (from spacy) (1.1.3)\n",
            "Requirement already satisfied: srsly<3.0.0,>=2.4.3 in /usr/local/lib/python3.11/dist-packages (from spacy) (2.5.1)\n",
            "Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in /usr/local/lib/python3.11/dist-packages (from spacy) (2.0.10)\n",
            "Requirement already satisfied: weasel<0.5.0,>=0.1.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (0.4.1)\n",
            "Requirement already satisfied: typer<1.0.0,>=0.3.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (0.15.1)\n",
            "Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (4.67.1)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (2.32.3)\n",
            "Requirement already satisfied: pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4 in /usr/local/lib/python3.11/dist-packages (from spacy) (2.10.6)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from spacy) (3.1.5)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.11/dist-packages (from spacy) (75.1.0)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (24.2)\n",
            "Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (3.5.0)\n",
            "Requirement already satisfied: numpy>=1.19.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (1.26.4)\n",
            "Requirement already satisfied: language-data>=1.2 in /usr/local/lib/python3.11/dist-packages (from langcodes<4.0.0,>=3.2.0->spacy) (1.3.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy) (2.27.2)\n",
            "Requirement already satisfied: typing-extensions>=4.12.2 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy) (4.12.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy) (2025.1.31)\n",
            "Requirement already satisfied: blis<0.8.0,>=0.7.8 in /usr/local/lib/python3.11/dist-packages (from thinc<8.3.0,>=8.2.2->spacy) (0.7.11)\n",
            "Requirement already satisfied: confection<1.0.0,>=0.0.1 in /usr/local/lib/python3.11/dist-packages (from thinc<8.3.0,>=8.2.2->spacy) (0.1.5)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy) (8.1.8)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy) (1.5.4)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy) (13.9.4)\n",
            "Requirement already satisfied: cloudpathlib<1.0.0,>=0.7.0 in /usr/local/lib/python3.11/dist-packages (from weasel<0.5.0,>=0.1.0->spacy) (0.20.0)\n",
            "Requirement already satisfied: smart-open<8.0.0,>=5.2.1 in /usr/local/lib/python3.11/dist-packages (from weasel<0.5.0,>=0.1.0->spacy) (7.1.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->spacy) (3.0.2)\n",
            "Requirement already satisfied: marisa-trie>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from language-data>=1.2->langcodes<4.0.0,>=3.2.0->spacy) (1.2.1)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy) (2.18.0)\n",
            "Requirement already satisfied: wrapt in /usr/local/lib/python3.11/dist-packages (from smart-open<8.0.0,>=5.2.1->weasel<0.5.0,>=0.1.0->spacy) (1.17.2)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy) (0.1.2)\n",
            "Collecting ru-core-news-sm==3.7.0\n",
            "  Downloading https://github.com/explosion/spacy-models/releases/download/ru_core_news_sm-3.7.0/ru_core_news_sm-3.7.0-py3-none-any.whl (15.3 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m15.3/15.3 MB\u001b[0m \u001b[31m30.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: spacy<3.8.0,>=3.7.0 in /usr/local/lib/python3.11/dist-packages (from ru-core-news-sm==3.7.0) (3.7.5)\n",
            "Collecting pymorphy3>=1.0.0 (from ru-core-news-sm==3.7.0)\n",
            "  Downloading pymorphy3-2.0.3-py3-none-any.whl.metadata (1.9 kB)\n",
            "Collecting dawg2-python>=0.8.0 (from pymorphy3>=1.0.0->ru-core-news-sm==3.7.0)\n",
            "  Downloading dawg2_python-0.9.0-py3-none-any.whl.metadata (7.5 kB)\n",
            "Collecting pymorphy3-dicts-ru (from pymorphy3>=1.0.0->ru-core-news-sm==3.7.0)\n",
            "  Downloading pymorphy3_dicts_ru-2.4.417150.4580142-py2.py3-none-any.whl.metadata (2.0 kB)\n",
            "Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.11 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (3.0.12)\n",
            "Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (1.0.5)\n",
            "Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (1.0.12)\n",
            "Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (2.0.11)\n",
            "Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (3.0.9)\n",
            "Requirement already satisfied: thinc<8.3.0,>=8.2.2 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (8.2.5)\n",
            "Requirement already satisfied: wasabi<1.2.0,>=0.9.1 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (1.1.3)\n",
            "Requirement already satisfied: srsly<3.0.0,>=2.4.3 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (2.5.1)\n",
            "Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (2.0.10)\n",
            "Requirement already satisfied: weasel<0.5.0,>=0.1.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (0.4.1)\n",
            "Requirement already satisfied: typer<1.0.0,>=0.3.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (0.15.1)\n",
            "Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (4.67.1)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (2.32.3)\n",
            "Requirement already satisfied: pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (2.10.6)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (3.1.5)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (75.1.0)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (24.2)\n",
            "Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (3.5.0)\n",
            "Requirement already satisfied: numpy>=1.19.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (1.26.4)\n",
            "Requirement already satisfied: language-data>=1.2 in /usr/local/lib/python3.11/dist-packages (from langcodes<4.0.0,>=3.2.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (1.3.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (2.27.2)\n",
            "Requirement already satisfied: typing-extensions>=4.12.2 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (4.12.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (2025.1.31)\n",
            "Requirement already satisfied: blis<0.8.0,>=0.7.8 in /usr/local/lib/python3.11/dist-packages (from thinc<8.3.0,>=8.2.2->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (0.7.11)\n",
            "Requirement already satisfied: confection<1.0.0,>=0.0.1 in /usr/local/lib/python3.11/dist-packages (from thinc<8.3.0,>=8.2.2->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (0.1.5)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (8.1.8)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (1.5.4)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (13.9.4)\n",
            "Requirement already satisfied: cloudpathlib<1.0.0,>=0.7.0 in /usr/local/lib/python3.11/dist-packages (from weasel<0.5.0,>=0.1.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (0.20.0)\n",
            "Requirement already satisfied: smart-open<8.0.0,>=5.2.1 in /usr/local/lib/python3.11/dist-packages (from weasel<0.5.0,>=0.1.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (7.1.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (3.0.2)\n",
            "Requirement already satisfied: marisa-trie>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from language-data>=1.2->langcodes<4.0.0,>=3.2.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (1.2.1)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (2.18.0)\n",
            "Requirement already satisfied: wrapt in /usr/local/lib/python3.11/dist-packages (from smart-open<8.0.0,>=5.2.1->weasel<0.5.0,>=0.1.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (1.17.2)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy<3.8.0,>=3.7.0->ru-core-news-sm==3.7.0) (0.1.2)\n",
            "Downloading pymorphy3-2.0.3-py3-none-any.whl (53 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m53.8/53.8 kB\u001b[0m \u001b[31m3.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading dawg2_python-0.9.0-py3-none-any.whl (9.3 kB)\n",
            "Downloading pymorphy3_dicts_ru-2.4.417150.4580142-py2.py3-none-any.whl (8.4 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.4/8.4 MB\u001b[0m \u001b[31m37.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: pymorphy3-dicts-ru, dawg2-python, pymorphy3, ru-core-news-sm\n",
            "Successfully installed dawg2-python-0.9.0 pymorphy3-2.0.3 pymorphy3-dicts-ru-2.4.417150.4580142 ru-core-news-sm-3.7.0\n",
            "\u001b[38;5;2m✔ Download and installation successful\u001b[0m\n",
            "You can now load the package via spacy.load('ru_core_news_sm')\n",
            "\u001b[38;5;3m⚠ Restart to reload dependencies\u001b[0m\n",
            "If you are in a Jupyter or Colab notebook, you may need to restart Python in\n",
            "order to load all the package's dependencies. You can do this by selecting the\n",
            "'Restart kernel' or 'Restart runtime' option.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import nltk\n",
        "nltk.download(\"stopwords\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Yllnt1YjHHL2",
        "outputId": "006e22a0-b7a4-4723-b25a-9dfe35d6f138"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package stopwords to /root/nltk_data...\n",
            "[nltk_data]   Unzipping corpora/stopwords.zip.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import spacy\n",
        "from aiogram import Bot, Dispatcher, types\n",
        "from aiogram.types import ReplyKeyboardMarkup, KeyboardButton\n",
        "from aiogram.filters import Command\n",
        "from sklearn.feature_extraction.text import TfidfVectorizer\n",
        "from sklearn.metrics.pairwise import cosine_similarity\n",
        "import gensim\n",
        "from gensim.models import Word2Vec\n",
        "import json\n",
        "import numpy as np\n",
        "\n",
        "# Загружаем SpaCy модель для русского языка\n",
        "nlp = spacy.load(\"ru_core_news_sm\")\n",
        "\n",
        "# Инициализация бота\n",
        "dp = Dispatcher()\n",
        "bot = Bot(token='my_token')\n",
        "\n",
        "# Функция для лемматизации текста с использованием spaCy\n",
        "def lemmatize_text(text):\n",
        "    doc = nlp(text)\n",
        "    lemmas = [token.lemma_ for token in doc]\n",
        "    return \" \".join(lemmas)\n",
        "\n",
        "# Загрузка FAQ из JSON\n",
        "!wget https://raw.githubusercontent.com/vifirsanova/compling/main/tasks/task3/faq.json\n",
        "with open('faq.json', encoding='utf-8') as f:\n",
        "    data = json.load(f)\n",
        "\n",
        "# Извлекаем вопросы и ответы\n",
        "faq_questions = [q['question'] for i in data.values() for q in i]\n",
        "faq_answers = [q['answer'] for i in data.values() for q in i]\n",
        "\n",
        "# Лемматизируем вопросы из FAQ\n",
        "faq_questions_lemmatized = [lemmatize_text(q) for q in faq_questions]\n",
        "\n",
        "# Преобразование вектора для TF-IDF (используем лемматизированные вопросы)\n",
        "vectorizer = TfidfVectorizer()\n",
        "tfidf_matrix = vectorizer.fit_transform(faq_questions_lemmatized)\n",
        "\n",
        "# Инициализация модели Word2Vec\n",
        "sentences = [q.split() for q in faq_questions_lemmatized]\n",
        "word2vec_model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)\n",
        "\n",
        "\n",
        "# Функция для получения ответа с использованием TF-IDF\n",
        "def get_tfidf_answer(question):\n",
        "    # Лемматизируем запрос\n",
        "    lemmatized_question = lemmatize_text(question)\n",
        "    # Преобразуем запрос в вектор\n",
        "    query_vec = vectorizer.transform([lemmatized_question])\n",
        "    # Вычисляем косинусное сходство\n",
        "    similarities = cosine_similarity(query_vec, tfidf_matrix)\n",
        "    # Ищем индекс наиболее похожего вопроса\n",
        "    best_match_idx = similarities.argmax()\n",
        "    return faq_answers[best_match_idx]\n",
        "\n",
        "# Функция для усреднения векторов слов в вопросе\n",
        "def sentence_vector(sentence, model):\n",
        "    words = sentence.split()\n",
        "    vectors = [model.wv[word] for word in words if word in model.wv]\n",
        "    return np.mean(vectors, axis=0) # Берем среднее значение по всем векторам, чтобы одно предложение представлял один вектор\n",
        "\n",
        "# Векторизуем вопросы\n",
        "faq_vectors = np.array([sentence_vector(query, word2vec_model) for query in faq_questions_lemmatized])\n",
        "\n",
        "# Функция для получения ответа с использованием Word2Vec\n",
        "def get_word2vec_answer(question):\n",
        "    # Лемматизируем запрос\n",
        "    lemmatized_question = lemmatize_text(question)\n",
        "\n",
        "    # Генерируем вектор запроса, усреднив векторы всех слов\n",
        "    query_vector = sentence_vector(lemmatized_question, word2vec_model).reshape(1, -1)\n",
        "\n",
        "    # Оценка косинусного сходства с каждым вопросом из FAQ\n",
        "    similarities = cosine_similarity(query_vector, faq_vectors)\n",
        "    best_match_idx = similarities.argmax()\n",
        "\n",
        "    return faq_answers[best_match_idx]\n",
        "\n",
        "\n",
        "# Обработка команды /start\n",
        "@dp.message(Command(\"start\"))\n",
        "async def welcome(message: types.Message):\n",
        "    keyboard = ReplyKeyboardMarkup(\n",
        "        keyboard=[ [KeyboardButton(text='О компании')], [KeyboardButton(text='Пожаловаться')] ],\n",
        "        resize_keyboard=True\n",
        "    )\n",
        "    await message.answer('Привет! Я бот, помогу ответить на Ваши вопросы.', reply_markup=keyboard)\n",
        "\n",
        "# Обработка нажатия кнопки 'О компании'\n",
        "@dp.message(lambda message: message.text == 'О компании')\n",
        "async def about_company(message: types.Message):\n",
        "    await message.answer('Наша компания занимается доставкой товаров по всей стране.')\n",
        "\n",
        "# Обработка нажатия кнопки 'Пожаловаться'\n",
        "@dp.message(lambda message: message.text == 'Пожаловаться')\n",
        "async def complain(message: types.Message):\n",
        "    await message.answer('Отправьте скриншот, на котором показана Ваша проблема.')\n",
        "\n",
        "# Обработка изображений\n",
        "@dp.message(lambda message: message.content_type == \"photo\")\n",
        "async def handle_photo(message: types.Message):\n",
        "    file_id = message.photo[-1].file_id\n",
        "    file = await bot.get_file(file_id)\n",
        "    filename = file.file_path.split(\"/\")[-1]\n",
        "    filesize = message.photo[0].file_size\n",
        "    await message.answer(f'Ваш запрос передан специалисту. Название файла: {filename}, размер: {filesize} байт')\n",
        "\n",
        "# Обработка вопросов пользователей\n",
        "@dp.message()\n",
        "async def answer_question(message: types.Message):\n",
        "    question = message.text\n",
        "    # Ответ на основе TF-IDF\n",
        "    tfidf_answer = get_tfidf_answer(question)\n",
        "    # Ответ на основе Word2Vec\n",
        "    word2vec_answer = get_word2vec_answer(question)\n",
        "    # Отправляем оба ответа пользователю\n",
        "    await message.answer(f\"Ответ на основе TF-IDF: {tfidf_answer}\")\n",
        "    await message.answer(f\"Ответ на основе Word2Vec: {word2vec_answer}\")\n",
        "\n",
        "\n",
        "# Основной цикл\n",
        "async def main():\n",
        "    await dp.start_polling(bot)\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    await main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f7jFq9YcHKHS",
        "outputId": "352ffe7f-ff6b-40bd-afba-2f845435ab28"
      },
      "execution_count": 4,
      "outputs": [
        {
          "metadata": {
            "tags": null
          },
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "--2025-02-27 11:15:13--  https://raw.githubusercontent.com/vifirsanova/compling/main/tasks/task3/faq.json\n",
            "Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...\n",
            "Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 2876 (2.8K) [text/plain]\n",
            "Saving to: ‘faq.json’\n",
            "\n",
            "\rfaq.json              0%[                    ]       0  --.-KB/s               \rfaq.json            100%[===================>]   2.81K  --.-KB/s    in 0s      \n",
            "\n",
            "2025-02-27 11:15:13 (40.7 MB/s) - ‘faq.json’ saved [2876/2876]\n",
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:aiogram.dispatcher:Received SIGINT signal\n"
          ]
        }
      ]
    }
  ]
}
