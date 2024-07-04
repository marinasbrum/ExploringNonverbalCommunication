{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMX0tsjOepLC+srBNC4mz+i",
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
        "<a href=\"https://colab.research.google.com/github/marinasbrum/ExploringNonverbalCommunication/blob/main/Emotional_Responses_Analysis.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Instalação de Pacotes:"
      ],
      "metadata": {
        "id": "Hw5W6KYo8fRt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install pandas\n",
        "!pip install matplotlib"
      ],
      "metadata": {
        "id": "3DW3bgK799yL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Importação de Bibliotecas:"
      ],
      "metadata": {
        "id": "FEG7RwLx-aaK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt"
      ],
      "metadata": {
        "id": "qdAPvmjM83Ni"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Leitura e Manipulação de Arquivos CSV:"
      ],
      "metadata": {
        "id": "B-S1Ju8t-h4u"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "teste = pd.read_csv('teste.csv')\n",
        "teste.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "_xOKBn6U-iC6",
        "outputId": "e3fdbb21-b87f-497e-c4cd-64928bf71f61"
      },
      "execution_count": 71,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Season  Episode   Time Influencer  \\\n",
              "0       1        1  02:58     Dwight   \n",
              "1       1        1  21:40        Pam   \n",
              "2       1        2  08:00     Dwight   \n",
              "3       1        2  10:34     Dwight   \n",
              "4       1        2  20:52        Pam   \n",
              "\n",
              "                                            Scenario Emotional_Responses  \\\n",
              "0                         Observando o Dwight cantar            Escárnio   \n",
              "1  Pam foi vítima de uma brincadeira de demissão ...              Tensão   \n",
              "2  Dwight respondendo uma pergunta de forma inade...            Escárnio   \n",
              "3  Perdeu um cliente para o Dwight por não ter co...          Frustração   \n",
              "4    Pam dormindo no ombro dele, não sabe se levanta          Satisfação   \n",
              "\n",
              "               Events Prank  \n",
              "0              Nenhum   Não  \n",
              "1              Nenhum   Não  \n",
              "2  Dia da diversidade   Não  \n",
              "3  Dia da diversidade   Não  \n",
              "4  Dia da diversidade   Não  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-03f85689-c484-4947-abf4-d25a0a4dec5e\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Season</th>\n",
              "      <th>Episode</th>\n",
              "      <th>Time</th>\n",
              "      <th>Influencer</th>\n",
              "      <th>Scenario</th>\n",
              "      <th>Emotional_Responses</th>\n",
              "      <th>Events</th>\n",
              "      <th>Prank</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>02:58</td>\n",
              "      <td>Dwight</td>\n",
              "      <td>Observando o Dwight cantar</td>\n",
              "      <td>Escárnio</td>\n",
              "      <td>Nenhum</td>\n",
              "      <td>Não</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>21:40</td>\n",
              "      <td>Pam</td>\n",
              "      <td>Pam foi vítima de uma brincadeira de demissão ...</td>\n",
              "      <td>Tensão</td>\n",
              "      <td>Nenhum</td>\n",
              "      <td>Não</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>08:00</td>\n",
              "      <td>Dwight</td>\n",
              "      <td>Dwight respondendo uma pergunta de forma inade...</td>\n",
              "      <td>Escárnio</td>\n",
              "      <td>Dia da diversidade</td>\n",
              "      <td>Não</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>10:34</td>\n",
              "      <td>Dwight</td>\n",
              "      <td>Perdeu um cliente para o Dwight por não ter co...</td>\n",
              "      <td>Frustração</td>\n",
              "      <td>Dia da diversidade</td>\n",
              "      <td>Não</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>20:52</td>\n",
              "      <td>Pam</td>\n",
              "      <td>Pam dormindo no ombro dele, não sabe se levanta</td>\n",
              "      <td>Satisfação</td>\n",
              "      <td>Dia da diversidade</td>\n",
              "      <td>Não</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-03f85689-c484-4947-abf4-d25a0a4dec5e')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-03f85689-c484-4947-abf4-d25a0a4dec5e button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-03f85689-c484-4947-abf4-d25a0a4dec5e');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-6c98d9e6-c787-44d7-b531-08725ba5ebe2\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-6c98d9e6-c787-44d7-b531-08725ba5ebe2')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-6c98d9e6-c787-44d7-b531-08725ba5ebe2 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "teste",
              "summary": "{\n  \"name\": \"teste\",\n  \"rows\": 10,\n  \"fields\": [\n    {\n      \"column\": \"Season\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 1,\n        \"max\": 1,\n        \"num_unique_values\": 1,\n        \"samples\": [\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Episode\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 1,\n        \"max\": 6,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Time\",\n      \"properties\": {\n        \"dtype\": \"object\",\n        \"num_unique_values\": 10,\n        \"samples\": [\n          \"20:36\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Influencer\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Pam\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Scenario\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 10,\n        \"samples\": [\n          \"Soltou um elogio sobre sua habilidade no basquete para seu noivo\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Emotional_Responses\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Esc\\u00e1rnio\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Events\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"Nenhum\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Prank\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Sim\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 71
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Convertendo a coluna para confirmar o formato de min:seg :"
      ],
      "metadata": {
        "id": "NRB_XgOc_HRu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "teste['Time'] = pd.to_datetime(teste['Time'], format='%M:%S').dt.time"
      ],
      "metadata": {
        "id": "yldBWYRT_Jc4"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "uNxWK69jC08E"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "looks_season1 = teste.groupby('Episode').size().reset_index(name='Quantidade')\n",
        "looks = teste['Episode'].nunique()\n",
        "episodes = teste.shape[0]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W-nweyUZC1GD",
        "outputId": "4a65f2e8-4d3e-45b1-e18e-19bdadead0ca"
      },
      "execution_count": 90,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6\n",
            "10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(episodes, looks))\n",
        "plt.plot(looks_season1['Episode'], looks_season1['Quantidade'], marker='o', linestyle='-', color='b')\n",
        "plt.yticks(range(int(min(looks_season1['Quantidade'])), int(max(looks_season1['Quantidade'])) + 1))\n",
        "plt.title('Número de Olhadas de Jim Halpert para a Câmera na Primeira Temporada')\n",
        "plt.xlabel('Episódios')\n",
        "plt.ylabel('Olhadas por Episódio')\n",
        "plt.grid(True)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 565
        },
        "id": "Vwn3XB-XEAoj",
        "outputId": "12d0478b-bbad-4fad-beba-993304d3eda4"
      },
      "execution_count": 95,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "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J8Qk8vX6+uuvVahQIXuGyNcs0rFjx9S+fXvlzZtXSZMmVerUqVW/fv1n6nr5/PPPK02aNDpy5MgT/8742j/E5fmP6f048n/n0KFDqlatmgIDA/X2229LerZtNS4+/fRTFS1aVEmTJlWqVKnUsGFDnThxIso8z/rcRH6u2L9/vxo0aKCgoCClTp1aXbp00d27d6PMe//+fQ0fPly5cuWSv7+/smfPrv79+0d738iePbveeOMNrVu3TsWKFVPSpEk1e/ZsSda+VyL+cCQIUeTIkUPvvvuu5s6dq759+8b5aFBcvPXWW8qfP79Gjx6t7777TiNGjFCqVKk0e/ZsvfbaaxozZow+++wz9ezZUy+99JJeffVVSeY3tTVr1tQvv/yiNm3aKH/+/NqzZ48mTpyof//9V19//XWU9WzYsEFLlixRx44dlSZNGmXPnl3//POPypQpo6CgIPXu3Vu+vr6aPXu2ypUrZ9/ZxsYwDNWqVUu//PKL3nvvPeXPn18rVqxQ06ZNo837zz//qFSpUsqcObP69u2rZMmSacmSJapdu7aWLVumOnXqxLqeb7/9VpL07rvvxni/j4+PGjdurKFDh2rLli2qWLHiY5/vBg0aKEeOHBo1apR27typefPmKV26dBozZox9npkzZ6pgwYKqWbOmfHx89O2336p9+/aKiIiIcrL1oEGDNGLECFWrVk3VqlXTzp07VblyZd27dy/KOg8fPqyvv/5a9evXV44cOXTu3DnNnj1bZcuW1d69e+3b09y5c9W5c2e9+eab9jetv/76S7/99psaN24c6990584dVahQQcePH1fnzp2VKVMmffLJJ9qwYUO0eTds2KCqVauqaNGiGjx4sLy8vOxvZD///LNefvnlxz5/cXXlyhW98cYbatiwoerXr6+ZM2eqYcOG+uyzz9S1a1e99957aty4sT788EO9+eabOnHihAIDA5+43Nu3b8d43s+jhawkLV26VLdv31a7du2UOnVq/f7775o6dapOnjyppUuXPnFdmzZt0pdffqnOnTvL399fM2bM0Ouvv67ff//dfi7guXPn9Morr9g/lKZNm1Zr1qxRy5Ytdf36dXXt2jXKMocPHy4/Pz/17NlToaGhqly5sjp37qwpU6aof//+9iMXTzqCER4ertdff12vvPKKxo4dq7Vr12rw4MG6f/++hg0bZp9v8uTJ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9BMnTuibb75R5cqV5e3tLW9vb9WrV0/Lli3T33//He3xcX0+I7sWOfrBdNq0afa2YRiaNm2afH19VaFCBUnmc2Cz2aIciT569Gi0kSMf51mW8ayvwXvvvaeMGTOqR48e9gLvYefPn9eIESNiXde9e/ecvu911mse133Cs4ppPVOnTn1s7wRX5qznP6blSs+2v4hN3bp15e3traFDh0Z7LQzDiLbfd4bp06dHuR35vhx5Xadq1apJiv5+Fdmz5EmjPkrWvlcifnEkCI/1/vvv65NPPtGBAweinTPTqlUrjR49Wq1atVKxYsW0efPmGN/An1WTJk20ZMkSvffee9q4caNKlSql8PBw7d+/X0uWLLGP6f84I0aM0Pr161W6dGm1b99ePj4+mj17tkJDQzV27NjHPrZGjRoqVaqU+vbtq6NHj6pAgQJavnx5jH2np0+frtKlS+v5559X69atlTNnTp07d05bt27VyZMnn3gNgI8//lgVKlRQrVq11LhxY5UpU0ahoaFavny5fvrpJ7311lvq1avXk5+0OKhcubL8/PxUo0YNtW3bVjdv3tTcuXOVLl26KEVc2rRp1bNnT40aNUpvvPGGqlWrpl27dmnNmjXRvrF64403NGzYMDVv3lwlS5bUnj179Nlnn0U7p6Ny5crKkCGDSpUqpfTp02vfvn2aNm2aqlev/tjznVq3bq1p06bp3Xff1R9//KGMGTPqk08+iTb8rZeXl+bNm6eqVauqYMGCat68uTJnzqxTp05p48aNCgoKsg9J7u7y5cunXLlyqWfPnjp16pSCgoK0bNmyOJ97JEmFChVSlSpVogyRLSlK18TRo0dr48aNKl68uFq3bq0CBQro8uXL2rlzp3744Qddvnz5iet54YUX5O3trTFjxujatWvy9/e3X3sjNkmSJNHatWvVtGlTFS9eXGvWrNF3332n/v37249SVa9eXRMmTNDrr7+uxo0b6/z585o+fbpy585t70L6JM+yjGd9DVKmTKkVK1aoWrVqeuGFF/TOO+/YB6rYuXOnPv/8c5UoUUKS+WVJypQp1bRpU3Xu3Fk2m02ffPKJ07tZSs55zeO6T3hWb7zxhj755BMFBwerQIEC2rp1q3744Qe3Pr/CGc//o5yxv4hNrly5NGLECPXr109Hjx5V7dq1FRgYqCNHjmjFihVq06aNevbs+czrediRI0dUs2ZNvf7669q6das+/fRTNW7cWEWKFJEkFSlSRE2bNtWcOXPsXUl///13ffTRR6pdu7bKly//xHVY+V6JeBZfw87BvTw8RPajIofafHRI49u3bxstW7Y0goODjcDAQKNBgwbG+fPnYx2y+eHhbCOXmyxZsmjre3Q4bsMwh6odM2aMUbBgQcPf399ImTKlUbRoUWPo0KHGtWvX7PNJMjp06BDj37hz506jSpUqRvLkyY2AgACjfPnyxq+//vrE58YwDOPSpUtGkyZNjKCgICM4ONho0qSJsWvXrhiHPD506JDx7rvvGhkyZDB8fX2NzJkzG2+88Ybx1VdfxWldN27cMIYMGWIULFjQSJo0qREYGGiUKlXKWLRoUZRhNx/+m+PyfEe+xpHDmRqGYaxcudIoXLiwkSRJEiN79uzGmDFjjAULFkSbLzw83Bg6dKiRMWNGI2nSpEa5cuWMv//+28iWLVu0YT979Ohhn69UqVLG1q1bjbJlyxply5a1zzd79mzj1VdfNVKnTm34+/sbuXLlMnr16hXltYzNsWPHjJo1axoBAQFGmjRpjC5duhhr166NcejlXbt2GXXr1rWvJ1u2bEaDBg2MH3/88bHrOHz4sCHJmDBhgn1abEPgxjTUd7Zs2Yzq1atHm/647TNSTMNzPyym13fv3r1GxYoVjeTJkxtp0qQxWrdubR9GOKZhZWPK9Omnnxp58uQx/P39jRdffDHGYazPnTtndOjQwQgJCTF8fX2NDBkyGBUqVDDmzJljnyfyeVq6dGmM+efOnWvkzJnT8Pb2fuJw2ZH7iEOHDhmVK1c2AgICjPTp0xuDBw+ONrzs/Pnz7fnz5ctnLFy48LF/b0ziuoyYxPU1eJzTp08b3bp1M5577jkjSZIkRkBAgFG0aFFj5MiRUf43tmzZYrzyyitG0qRJjUyZMhm9e/e2DyPs7O3zWV/zuO4TYhPb6/XovufKlStG8+bNjTRp0hjJkyc3qlSpYuzfvz/afI6u52GP+zvja/8Ql+c/tiGyY3p/NQznbKuGEX2I7EjLli0zSpcubSRLlsxIliyZkS9fPqNDhw7GgQMH7PM863MT+X+5d+9e48033zQCAwONlClTGh07djTu3LkT5bFhYWHG0KFDjRw5chi+vr5GSEiI0a9fvyjDyT9u3YZh3Xsl4pfNMOLh6yMAcGN//fWXihQponnz5kUZwj0xstls6tChQ5QuZ66iWbNm+uqrr2Ls0gjAcw0ZMkRDhw7VhQsXOIcGT41zggDgEZHXL4rLKHwAAMD9cE4QAPy/rVu3auPGjRo7dqzy5s0b5YJ9AAAg8aAIAoD/N3v2bC1dulRlypTR1KlTo11jAwAAJA6cEwQAAADAo/A1JwAAAACPQhEEAAAAwKO4/TlBEREROn36tAIDA2Wz2ayOAwAAAMAihmHoxo0bypQp02PP7XX7Iuj06dMKCQmxOgYAAAAAF3HixAllyZIl1vvdvggKDAyUZP6hQUFBlmYJCwvT999/r8qVK8vX19fSLHAPbDNwFNsMHMU2A0exzcARrra9XL9+XSEhIfYaITZuXwRFdoELCgpyiSIoICBAQUFBLrERwPWxzcBRbDNwFNsMHMU2A0e46vbypNNkGBgBAAAAgEehCAIAAADgUSiCAAAAAHgUiiAAAAAAHoUiCAAAAIBHoQgCAAAA4FEoggAAAAB4FIogAAAAAB6FIggAAACAR6EIAgAAAOBRKIIAAAAAeBSKIAAAAAAehSIIAAAAgEehCAIsEh4ubdpk0+bNmbVpk03h4VYnAgAA8AyWFkEzZ85U4cKFFRQUpKCgIJUoUUJr1qyxMhKQIJYvl7JnlypV8tGECcVUqZKPsmc3pwMAACB+WVoEZcmSRaNHj9Yff/yhHTt26LXXXlOtWrX0zz//WBkLiFfLl0tvvimdPBl1+qlT5nQKIQAAgPhlaRFUo0YNVatWTXny5NFzzz2nkSNHKnny5Nq2bZuVsYB4Ex4udekiGUb0+yKnde0qusYBAADEIx+rA0QKDw/X0qVLdevWLZUoUSLW+UJDQxUaGmq/ff36dUlSWFiYwsLC4j3n40Su3+occF2bNtl08mTs/3aGIZ04IW3ceF9ly8ZQKcHjsZ+Bo9hm4Ci2GTjC1baXuOawGUZM30knnD179qhEiRK6e/eukidPrsWLF6tatWqxzj9kyBANHTo02vTFixcrICAgPqMCz2zz5syaMKHYE+fr3n2HXn31VAIkAgAASDxu376txo0b69q1awoKCop1PsuLoHv37un48eO6du2avvrqK82bN0+bNm1SgQIFYpw/piNBISEhunjx4mP/0IQQFham9evXq1KlSvL19bU0C1zTpk02Var05AOw69dzJAgxYz8DR7HNwFFsM3CEq20v169fV5o0aZ5YBFneHc7Pz0+5c+eWJBUtWlTbt2/X5MmTNXv27Bjn9/f3l7+/f7Tpvr6+LvHES66VBa6lfHkpY0bpzJmY77fZpCxZpPLlfeTtnbDZ4F7Yz8BRbDNwFNsMHOEq20tcM7jcdYIiIiKiHOkBEhNvb3No7NgYhjRpkiiAAAAA4pGlR4L69eunqlWrKmvWrLpx44YWL16sn376SevWrbMyFhBvliyRtm6VvLykNGmk8+ej3p8unVS5sjXZAAAAPIWlR4LOnz+vd999V3nz5lWFChW0fft2rVu3TpUqVbIyFhAvzp2T2rc32wMHSqdPm+f+dO++Q998c19Zs5pFUZ8+1uYEAABI7Cw9EjR//nwrVw8kGMOQ2rWTLl2SXnhB6t/f7PJWtqyhW7dOqWrVIlqwQKpYUZoxQ6pbV6pQwerUAAAAiZPLnRMEJEaffy6tWCH5+kqLFkl+ftHnqVDhwZGili2lGzcSNCIAAIDHoAgC4tmZM1LHjmZ74ECpSJHY5x0zRsqRQzp2TOrVK2HyAQAAeBqKICAeGYbUtq105Yr0v/9Jffs+fv7kyaUFC8z27NnS99/Hf0YAAABPQxEExKNPP5W+/dbsBvfRR+bvJylXTurUyWy3aiVduxavEQEAADwORRAQT06dkjp3NttDh0qFCsX9saNGSblySSdOSD16xE8+AAAAT0URBMQDw5DatJGuXpVeesnx83uSJZMWLpRsNmn+fGnNmniJCQAA4JEogoB48NFH0urV5ihwixZJPk8xGH2ZMlKXLma7dWuzoAIAAMCzowgCnOzkyQfFy/DhUoECT7+skSOlPHnMrnXdujknHwAAgKejCAKcyDDMwQyuX5deeeXZz+cJCDCPJNls5u9Vq5yREgAAwLNRBAFONH++tG6dlCSJWbR4ez/7MkuWfFBMtWljDrcNAACAp0cRBDjJ8eNS9+5me8QIKW9e5y172DBzeWfOPOhqBwAAgKdDEQQ4gWFILVtKN26YR266dnXu8pMmNY8seXlJn3wiffONc5cPAADgSSiCACeYM0f64QezWFm40Dnd4B71yisPhtpu21a6dMn56wAAAPAEFEHAMzpy5ME5O6NGSc89F3/rGjLEHG3u3DmpU6f4Ww8AAEBiRhEEPIOICLMb3K1b5nV94rsweXjAhc8/l5Yvj9/1AQAAJEYUQcAzmDVL2rjRHMp64ULznJ349tJLUp8+Zvu996QLF+J/nQAAAIkJRRDwlA4ffnCOzpgxUq5cCbfuQYOkQoXMAqhjx4RbLwAAQGJAEQQ8hYgIqXlz6fZtqVw5qX37hF2/v7/00Udmt7glS8wfAAAAxA1FEPAUpk2TNm+WkiWTFixImG5wj/rf/6T33zfbHTpI588nfAYAAAB3RBEEOOi//6S+fc32hx9KOXJYl+X996UiRaSLF82jUYZhXRYAAAB3QREEOCA8XGrWTLpzR6pQwbxej5X8/MzR4nx8pGXLpC+/tDYPAACAO6AIAhwwZYq0ZYuUPLk0f7413eAe9cIL0sCBZrtDB+nsWUvjAAAAuDwX+AgHuIcDB6T+/c32hAlStmzW5nlYv37Siy9Kly+bw2bTLQ4AACB2FEFAHISHm6PB3b0rVa4stWpldaKofH3N0eJ8faVvvpE++8zqRAAAAK6LIgiIg4kTpa1bpaAgad48yWazOlF0zz8vDR5stjt3lk6ftjYPAACAq6IIAp5g3z5pwACzPXGiFBJibZ7H6dNHKlpUunLFHLSBbnEAAADRUQQBj3H/vjkaXGioVLWq2SXOlfn4mN3i/PykVaukjz+2OhEAAIDroQgCHmPcOOn336XgYGnuXNfsBveoggWlYcPMdpcu0qlT1uYBAABwNRRBQCz++efBOTaTJ0uZM1ubxxE9ekgvvyxduya1bk23OAAAgIdRBAExCAuTmjaV7t2T3nhDevddqxM5xsfHvIiqv7+0Zo20cKHViQAAAFwHRRAQg7FjpT/+kFKmlGbPdo9ucI/Kn18aMcJsd+smHT9ubR4AAABXQREEPOKvv6ShQ8321KlSpkzW5nkW3bpJJUpI16+b1zaiWxwAAABFEBBFWJg5GlxYmFSrltS4sdWJno23t9ktLkkSaf16c3AHAAAAT0cRBDxk1Chp1y4pVSpp1iz37Ab3qOeekz74wGz36CEdO2ZtHgAAAKtRBAH/b/duafhwsz19upQhg6VxnKpzZ6l0aenmTalFCykiwupEAAAA1qEIAmSOAte0qXlx1Hr1pLfesjqRc3l7myPEJU0qbdhgDvYAAADgqSiCAJmjqP31l5QmjTRjRuLoBveo3LmlMWPMdq9e0pEj1uYBAACwCkUQPN7OnQ/OmZkxQ0qXzto88alDB6lsWenWLbrFAQAAz0URBI8WGmp2gwsPlxo0kOrXtzpR/PLykhYskJIlk376ySz6AAAAPA1FEDzasGHS33+bR3+mT7c6TcLImdO8GKwk9ekj/feftXkAAAASGkUQPNb27dLo0WZ71izzfCBP8d570muvSbdv0y0OAAB4HoogeKS7d82LokZESI0aSXXqWJ0oYXl5SfPnS8mTSz//LE2danUiAACAhEMRBI80ZIi0d6+UPr3nFgDZs0vjxpntfv2kf/+1NA4AAECCoQiCx9m2TfrwQ7M9e7aUOrW1eazUpo1UsaJ0547UvLk5QAQAAEBiRxEEj3LnzoNucE2aSLVqWZ3IWjab2S0uMFD69Vdp0iSrEwEAAMQ/iiB4lIEDpQMHpIwZpcmTrU7jGrJmlSZONNvvvy/t329tHgAAgPhGEQSP8euv0oQJZnvuXCllSmvzuJIWLaTXXzevm9SsGd3iAABA4kYRBI9w+7b54d4wzN/Vq1udyLXYbGZhGBws/fabNH681YkAAADiD0UQPML770sHD0qZMz/o+oWosmR5cE7QwIHm6HkAAACJEUUQEr2ff35w/s+8eVKKFJbGcWlNm5pHye7dM9v371udCAAAwPkogpCo3bplDv1sGFLLluZ5L4idzSbNmWMWijt2PBhKHAAAIDGhCEKi1q+fdOiQFBLCeS5xlSmTNGWK2R48WNqzx9o8AAAAzkYRhETrp5+kqVPN9vz55kn/iJt33pFq1pTCwsyBJMLCrE4EAADgPBRBSJRu3jS7wUlS27ZSpUrW5nE3Nps0e7aUKpW0c6c0erTViQAAAJyHIgiJUu/e0tGjUrZsnNfytDJkeHAkbdgw6c8/rc0DAADgLBRBSHR+/FGaOdNsz58vBQZam8edNWok1aljjhLXrJk5ahwAAIC7owhConL9utSihdlu316qUMHaPO7OZjMLytSppd27pQ8+sDoRAADAs6MIQqLSq5d0/LiUI4c0ZozVaRKH9OmlGTPM9siR5jlCAAAA7owiCInG99+b17iRpIULpeTJrc2TmDRoINWvT7c4AACQOFAEIVG4dk1q1cpsd+oklS1rbZ7EaPp0KW1a87pBw4dbnQYAAODpUQQhUejRQzpxQsqVSxo1yuo0iVPatA8GnBg1Stqxw9o8AAAAT4siCG5vzRpzFDibzewGlyyZ1YkSr3r1pIYNpfBwqWlTKTTU6kQAAACOowiCW7ty5UE3uK5dpTJlLI3jEaZNMwdL2LtXGjLE6jQAAACOowiCW+vWTTp9WsqTRxoxwuo0niF1amnWLLM9dqz022/W5gEAAHAURRDc1qpV0kcfmd3gFi2SAgKsTuQ5ateW3n5biogwR4u7e9fqRAAAAHFHEQS3dPmy1KaN2e7RQypZ0to8nmjKFClDBmn/fmnQIKvTAAAAxB1FENxSly7SmTNSvnzSsGFWp/FMqVI9uC7TuHHSr79amwcAACCuKILgdr75Rvr0U8nLy+wGlzSp1Yk8V40a5ihxhiE1by7duWN1IgAAgCejCIJbuXRJatvWbPfqJRUvbm0eSJMmSZkySf/+Kw0YYHUaAACAJ6MIglvp1Ek6d04qUIDhmV1FihTS3Llme+JE6ZdfLI0DAADwRBRBcBvLlkmffy55e5vd4JIksToRIlWrJrVo8aBb3K1bVicCAACIHUUQ3MKFC1K7dma7b1/ppZeszYPoJkyQsmSR/vtP6t/f6jQAAACxowiCW+jQwSyEChWSBg60Og1iEhwszZtntqdMkTZtsjYPAABAbCiC4PKWLJGWLjW7wX30keTvb3UixKZKFal1a7PdooV086a1eQAAAGJCEQSXdu6c1L692X7/fel//7M2D55s3Dgpa1bp8GGz6yIAAICroQiCyzIM8zygS5ekIkXMIgiuLyhImj/fbE+fLm3YYG0eAACAR1EEwWV98YW0YoXk42N2g/PzszoR4qpiRem998x2ixbSjRvW5gEAAHgYRRBc0tmzUseOZnvgQPNIENzL2LFS9uzSsWNS795WpwEAAHiAIgguxzDMowiXL0svvij162d1IjyNwEBpwQKzPWuWtH69tXkAAAAiUQTB5Xz2mfTNN5Kvr9kNztfX6kR4WuXLPzii17KldP26tXkAAAAkiiC4mNOnpU6dzPaQIdLzz1saB04werSUM6d04oTUo4fVaQAAACiC4EIMQ2rTRrp6VSpWjPNIEotkyaSFC832vHnS2rXW5gEAAKAIgsv4+GPpu+/MUeAWLTJHhUPi8OqrUpcuZrtVK7PQBQAAsApFEFzCyZMPPiQPGyYVLGhtHjjfBx9IuXNLp05J3btbnQYAAHgyiiBYzjCk1q2la9ek4sU5bySxCggwj/DZbGb3uO++szoRAADwVBRBsNyCBeZ5Iv7+dINL7EqVkrp1M9utW0tXrlibBwAAeCaKIFjq+PEHXaNGjJDy5bM2D+LfiBHSc89JZ85IXbtanQYAAHgiiiBYxjDMk+SvX5dKlHhwhACJW9Kk5vWfvLzMwTBWrrQ6EQAA8DQUQbDM3LnS+vVSkiRmNzhvb6sTIaG88orUs6fZbttWunTJ2jwAAMCzUATBEkePPhgAYdQos3sUPMvQoVL+/NLZs1LnzlanAQAAnoQiCAkuIkJq2VK6eVMqXZoPwJ4q8gigl5e0eLG0YoXViQAAgKegCEKCmz1b2rDBPDdk4ULzQzA808svS336mO333pMuXrQ2DwAA8Ax8/ESCOnxY6tXLbI8ZY148E55t8GDz4rjnz0sdO1qdBgAAeAKKICSYiAipRQvp1i2pbFmpQwerE8EV+Pubo8V5e0tffiktXWp1IgAAkNhRBCHBTJ8ubdokJUtmXiCVbnCIVLSo1K+f2W7f3jwqBAAAEF/4GIoE8d9/Ut++ZnvsWClnTmvzwPUMHCgVLmyeF9S+vXkdKQAAgPhAEYR4FxEhNW8u3b4tvfaaeQI88Cg/P3O0OB8fadkyackSqxMBAIDEiiII8W7KFOmXX6TkyaX58+kGh9i9+KI0YIDZbt/evIYQAACAs/FxFPHq338fnOsxfryUPbulceAG+veXXnhBunzZPGpItzgAAOBsFEGIN+HhUrNm0t27UqVKUuvWVieCO/D1NUeL8/WVvvnGvJAqAACAM1EEId5MmiRt3SoFBkrz5kk2m9WJ4C4KF5YGDTLbnTpJZ85YmwcAACQuFEGIF/v3S++/b7YnTpSyZrU2D9xPnz7m0NlXrkht29ItDgAAOA9FEJzu/n2paVMpNFR6/XXzAqmAo3x9zdHi/Pykb7+VPvnE6kQAACCxoAiC040fL/3+uxQcLM2dSzc4PL1ChaQhQ8x2587SqVOWxgEAAIkERRCcau/eB+dyTJokZcliaRwkAr16SS+9JF27JrVpQ7c4AADw7CiC4DSR3eDu3ZOqVzfbwLPy8TG7xfn7S6tXm20AAIBnQREEpxk7VtqxQ0qRQpozh25wcJ4CBaThw812167SiROWxgEAAG6OIghOsWfPg3M3pkyRMmWyNA4Soe7dpVdeka5fN685Rbc4AADwtCiC8MzCwsyub2FhUs2a0jvvWJ0IiZG3t9kVLkkSad06af58qxMBAAB3RRGEZzZ6tLRrl5QqlTR7Nt3gEH/y5pVGjjTb3btLx45ZmwcAALgniiA8k927pWHDzPa0aVKGDJbGgQfo0kUqVUq6cUNq2ZJucQAAwHEUQXhq9+5JzZqZo8LVrSs1bGh1IngCb29p4UIpaVLpxx/No48AAACOoAjCUxs5UvrzTyl1amnGDLrBIeHkySONGmW2e/aUjhyxNg8AAHAvFEF4Kjt3Sh98YLZnzJDSp7c2DzxPp05SmTLSrVtmt7iICKsTAQAAd0ERBIeFhj7oBle/vtSggdWJ4Im8vMxucQEB0saN0syZVicCAADugiIIDhs+3LwuUNq00vTpVqeBJ8uVy7xIryT17i0dOmRtHgAA4B4oguCQ7dvNIbEl85v3tGmtzQO0ayeVKyfdvi21aEG3OAAA8GQUQYizu3fNbnDh4eZIcPXqWZ0IMLvFLVggJUsmbd5sDtUOAADwOBRBiLOhQ6W9e81BEPigCVeSI4c0bpzZ7ttXOnjQ2jwAAMC1UQQhTn777cG5F7Nnm8NiA66kbVupYkXpzh2peXPziCUAAEBMKILwRHfumN3gIiKkd96RatWyOhEQnc0mzZsnBQZKW7ZIkydbnQgAALgqiiA80aBB0v79UoYMfLCEa8uWTRo/3my//7504IC1eQAAgGuiCMJj/frrgw+Vc+ZIqVJZmwd4klatpMqVow7kAQAA8DCKIMTq9m3zQ6RhSE2bSjVqWJ0IeLLIbnFBQdK2bdKECVYnAgAAroYiCLEaMMAcZStTJmnSJKvTAHEXEvJgmx040BzVEAAAIBJFEGL0888PPkTOmyelSGFlGsBxzZpJ1apJoaFm+/59qxMBAABXQRGEaG7dklq0MLvBtWghVa1qdSLAcTabeR5bcLC0ffuD6wgBAABQBCGa/v2l//6TsmThfAq4t8yZpSlTzPbgwdLff1ubBwAAuAaKIESxadODD43z55vfogPurEkTc1CPe/fMbnFhYVYnAgAAVqMIgt3Nm1Lz5ma7TRtzmGHA3dls0uzZUsqU0h9/SGPGWJ0IAABYjSIIdn36SEeOSFmzSh9+aHUawHkyZpSmTjXbw4ZJf/1lbR4AAGCtZyqCTp48qZMnTzorCyy0YYM0Y4bZnj/fvMYKkJg0bizVrm12h2valG5xAAB4MoeLoIiICA0bNkzBwcHKli2bsmXLphQpUmj48OGKiIiIj4yIZzdumKPASVK7dlLFitbmAeKDzSbNmiWlTi3t3i198IHViQAAgFUcLoLef/99TZs2TaNHj9auXbu0a9cuffDBB5o6daoGDhwYHxkRz3r1ko4dk7Jnl8aOtToNEH/Sp5emTzfbI0ZIu3ZZmwcAAFjDx9EHfPTRR5o3b55q1qxpn1a4cGFlzpxZ7du318iRI50aEPFr/XrzpHFJWrhQSp7c2jxAfGvQQFq6VFq2zBwtbvt2yc/P6lQAACAhOXwk6PLly8qXL1+06fny5dPly5edEgoJ4/p1qWVLs92xo1SunKVxgARhs5nnv6VJYw6QMGKE1YkAAEBCc7gIKlKkiKZNmxZt+rRp01SkSBGnhELC6NFDOnFCyplTGj3a6jRAwkmX7sFAIB98YA6dDQAAPIfD3eHGjh2r6tWr64cfflCJEiUkSVu3btWJEye0evVqpwdE/Fi7Vpo3z/xWfNEiKVkyqxMBCat+femtt6QvvzRHi/vjD8nf3+pUAAAgITh8JKhs2bL6999/VadOHV29elVXr15V3bp1deDAAZUpUyY+MsLJrl6VWrUy2507S7xs8FTTpplHhf75Rxo61Oo0AAAgoTh8JEiSMmXKxAAIbqxbN+nUKSl3boYJhmdLk8YcNrtuXWnMGPM6Qi+/bHUqAAAQ3+JUBP31118qVKiQvLy89NcTLrVeuHBhpwRD/PjuO7P7W2Q3uIAAqxMB1qpTx7yQ6uLF5mhxO3dKSZJYnQoAAMSnOBVBL7zwgs6ePat06dLphRdekM1mk2EY0eaz2WwKDw93ekg4x5UrUuvWZrt7d6lUKWvzAK5iyhRpwwZp3z5p8GDzqBAAAEi84lQEHTlyRGnTprW34Z66dJHOnJHy5pWGD7c6DeA6Uqc2r5dVq5Y0bpzZLe7/x30BAACJUJyKoGzZssXYhvtYuVL65BPJy8vsBpc0qdWJANdSs6bUpIn5f9KsmbR7N/8nAAAkVnEqglauXBnnBdasWfOpwyB+XLoktW1rtnv2lF55xdo8gKuaPFn64Qfp33+lgQPNo0IAACDxiVMRVLt27Si3Hz0nyGaz2ducE+R6OneWzp6V8udnGGDgcVKmlObOld54Q5owwRw0gXPnAABIfOJ0naCIiAj7z/fff68XXnhBa9assV8naPXq1frf//6ntWvXxndeOGj5cnPUK29v6aOPGPUKeJLq1aXmzSXDMLvF3b5tdSIAAOBsDl8nqGvXrpo1a5ZKly5tn1alShUFBASoTZs22rdvn1MD4ulduCC9957Z7t1beukla/MA7mLCBOn776X//pP695cmTbI6EQAAcKY4HQl62KFDh5QiRYpo04ODg3X06FEnRIKzdOxoFkIFC5rD/gKImxQppHnzzPbkydLmzZbGAQAATuZwEfTSSy+pe/fuOnfunH3auXPn1KtXL73MpdZdxtKl0pIlD7rB+ftbnQhwL6+/LrVqZbabN5du3bI2DwAAcB6Hi6AFCxbozJkzypo1q3Lnzq3cuXMra9asOnXqlObPnx8fGeGg8+el9u3Ndv/+UtGi1uYB3NX48VJIiHT4sNS3r9VpAACAszh8TlDu3Ln1119/af369dq/f78kKX/+/KpYsWKUUeJgDcMwC6CLF6XChaUBA6xOBLivoCBpwQKpUiVp2jSpbl2pfHmrUwEAgGflcBEkmUNiV65cWZUrV3Z2HjyjL7+Uli2TfHzMbnB+flYnAtxbxYrmdbZmz5ZatJD27JGSJ7c6FQAAeBYOd4eTpE2bNqlGjRr27nA1a9bUzz//7OxscNDZs1KHDmZ7wADphRcsjQMkGh9+KGXLJh09ao60CAAA3NsTi6ANGzbo5s2b9tuffvqpKlasqICAAHXu3FmdO3dWkiRJVKFCBS1evDhewyJ2hmEOh335sln89O9vdSIg8QgMNLvFSdLMmdIPP1ibBwAAPJsnFkFHjhxRmTJldObMGUnSiBEjNHbsWH355Zf2ImjJkiUaPXq0hg8fHu+BEbPFi6VvvpF8fc1ucL6+VicCEpfXXntwpLVlS+n6dWvzAACAp/fEIqhly5bq3bu3KlasKMksimrUqBFtvpo1a+rIkSPOT4gnOn1a6tTJbA8aZA6IAMD5Ro+WcuSQjh+Xeva0Og0AAHhacTonqFGjRlqxYoUkKSQkRD/++GO0eX744QeFhIQ4Nx2eyDDMk7avXDGHwu7Tx+pEQOKVPLm0cKHZnjtXWrfO2jwAAODpxHl0uOeee06S1KNHD3Xu3Fm7d+9WyZIlJUlbtmzRokWLNHny5PhJiVh98om0apU5CtyiRXSDA+Jb2bJS587SlCnmxVT//lsKDrY6FQAAcITDQ2S3a9dOGTJk0Pjx47VkyRJJ5nWCvvzyS9WqVcvpARG7U6fMD2OSNHSoVKiQtXkAT/HBB9Lq1dJ//0ndu0tcJxoAAPfyVNcJqlOnjurUqePsLHCAYUitW0vXrkkvv8z5CUBCSpbM7Bb36qvmqHH16knVqlmdCgAAxJXD1wk6ceKETp48ab/9+++/q2vXrpozZ45Tg+HxFi6U1qyR/P3Nts9TlbMAnlbp0lLXrma7dWvzvDwAAOAeHC6CGjdurI0bN0qSzp49q4oVK+r333/X+++/r2HDhjk9IKI7cULq1s1sDx8uFShgbR7AU40YIT33nDlCY+T/JAAAcH0OF0F///23Xn75ZUnSkiVL9Pzzz+vXX3/VZ599pkWLFjk7Hx5hGObJ2NevS6+8Yp6PAMAaAQHmgCReXub1ub791upEAAAgLhwugsLCwuTv7y/JHBa7Zs2akqR8+fLZL6iK+DNvnvT991KSJOaHL29vqxMBnq1ECalHD7Pdpo10+bK1eQAAwJM5XAQVLFhQs2bN0s8//6z169fr9ddflySdPn1aqVOndnpAPHDs2IMjPyNHSnnzWpsHgGnYMClfPuns2QcjNgIAANflcBE0ZswYzZ49W+XKlVOjRo1UpEgRSdLKlSvt3eTgfIYhtWwp3bwplSoldelidSIAkSKPzHp5SZ99Jn39tdWJAADA4zg8pli5cuV08eJFXb9+XSlTprRPb9OmjQICApwaDg/Mni39+KOUNKk5Ghzd4ADXUry41Lu3NHq01LatOXpcmjRWpwIAADFx+EiQJHl7e0cpgCQpe/bsSpcunVNCIaojRx5cB2j0aClPHmvzAIjZkCFSwYLS+fNSp05WpwEAALGJ05Gg//3vf/rxxx+VMmVKvfjii7LZbLHOu3PnTqeFgxQRIbVoId26ZV6YsWNHqxMBiI2/v9kt7pVXpC++MC+i+uabVqcCAACPilMRVKtWLfuIcLVr147PPHjEjBnSTz+ZQ/EuWGCecwDAdRUrJvXtaw5e0r69VLaslDat1akAAMDD4lQEDR48OMY24tehQ1KfPmZ77FgpVy5r8wCIm4EDpZUrpT17pA4dpCVLrE4EAAAe5vDACJF27Nihffv2SZIKFCigokWLOi0UzG5wzZtLt29L5ctL7dpZnQhAXEV2iyteXFq61CyCGjSwOhUAAIjkcOeqkydPqkyZMnr55ZfVpUsXdenSRS+99JJKly6tkydPxkdGjzR1qvTzz1Ly5HSDA9zR//4nvf++2W7fXjp3zto8AADgAYc/Wrdq1UphYWHat2+fLl++rMuXL2vfvn2KiIhQq1at4iOjx/n3X6lfP7P94YdS9uyWxgHwlPr3l4oUkS5dMo/mGobViQAAgPQURdCmTZs0c+ZM5c2b1z4tb968mjp1qjZv3uzUcJ4oPNzsBnfnjlSxonm9EQDuyc9P+ugjycdHWrHCHDEOAABYz+EiKCQkRGFhYdGmh4eHK1OmTE4J5ckmT5Z+/VUKDJTmzZMeMxo5ADdQpIg0aJDZ7tBBOnPG2jwAAOApiqAPP/xQnTp10o4dO+zTduzYoS5dumjcuHFODedp9u9/cA7BhAlStmzW5gHgHH37mucIXbliHt2lWxwAANZyuAhq1qyZdu/ereLFi8vf31/+/v4qXry4du7cqRYtWihVqlT2H8RdeLjUrJl0965UpYrUsqXViQA4i6+vOVqcr6/07bfSp59anQgAAM/m8BDZkyZNiocYGD9e+u03KShImjuXbnBAYvP889KQIebR3s6dpQoVJHoQAwBgDYeLoKZNm8ZHDo+2d++DcwYmTZJCQiyNAyCe9O5tDpCwY4fUpo15VIgvPAAASHhx7g63ZMkS3bt3z3775MmTioiIsN++ffu2xo4d69x0HuD+fbMbXGioVK2a2QaQOPn4mKPF+flJ331ntgEAQMKLcxHUqFEjXb161X67QIECOnr0qP32jRs31C/y4jaIsw8/lLZvl1KkkObM4VthILErUEAaNsxsd+kicY1pAAASXpyLIOOR4YwevQ3H7dkjDR5stidPljJntjYPgITRo4dUvLh0/brUqhWjxQEAkNAcHh0OzhEWZnZ9CwuTatSQmjSxOhGAhOLjY44W5+8vrVsnLVhgdSIAADwLRZBFxoyRdu6UUqaUZs+mGxzgafLlk0aONNvduknHj1ubBwAAT+LQ6HDr1q1TcHCwJCkiIkI//vij/v77b0mKcr4QHu/PPx+cEzBtmpQxo7V5AFija1dp+XLp11/Na4N9/z1fiAAAkBAcKoIeHR67bdu2UW7bePd+onv3HnSDq11batTI6kQArOLtLS1cKBUpIv3wgzk4yiO7VQAAEA/i3B0uIiLiiT/h4eHxmTVR+OADafduKXVqadYsvvUFPN1zz0mjRpntnj2lhwbdBAAA8YRzghLQrl0PzgGYPl1Kn97aPABcQ+fOUpky0s2bZre4hy7BBgAA4gFFUAK5d09q2tS8OOqbb0oNGlidCICr8PIyR4gLCJA2bDCPEgMAgPhDEZRAhg83rwuUJo15FIhucAAelju3NHq02e7VSzp82No8AAAkZhRBCWDHjgd9/mfMkNKlszYPANfUoYNUtqx0+7bUvDnd4gAAiC8OFUHh4eHavHkzw2E7IDTUHA0uPFx66y2pfn2rEwFwVZHd4pIlkzZvNo8aAwAA53OoCPL29lblypV15cqV+MqT6AwdKv3zj3n0Z9o0q9MAcHU5c0offmi2+/SR/vvP2jwAACRGDneHK1SokA7TWT1Ofv9dGjPGbM+aZZ4PBABP0ratVKGCdOfOgyPJAADAeRwugkaMGKGePXtq1apVOnPmjK5fvx7lB6a7d83R4CIipMaNpTp1rE4EwF14eUnz50vJk0tbtkhTplidCACAxMXH0QdUq1ZNklSzZk3ZHhrizDAM2Ww2Lpj6/wYNkvbvlzJk4AMMAMdlyyaNH28eFerfX6pWTcqb1+pUAAAkDg4XQRs3boyPHG4vPFzatMmmzZsz69gxL40bZ06fPVtKndrabADcU+vW0ldfSevXm6PF/fSTtHmzuZ9Jlsym8uUlb2+rUwIA4H4cLoLKli3rtJWPGjVKy5cv1/79+5U0aVKVLFlSY8aMUV43+7pz+XKpSxfp5EkfScXs08uWlWrWtC4XAPdms5nd4goVkrZuNQdYuXbN3M9MmCBlySJNnizVrWt1UgAA3MtTXSfo6tWrGj9+vFq1aqVWrVpp4sSJunbtmsPL2bRpkzp06KBt27Zp/fr1CgsLU+XKlXXr1q2niWWJ5culN9+UTp6Mft/mzeb9APC0QkKkt98224/uZk+dMvc/7GcAAHCMw0XQjh07lCtXLk2cOFGXL1/W5cuXNWHCBOXKlUs7d+50aFlr165Vs2bNVLBgQRUpUkSLFi3S8ePH9ccffzgayxLh4eYRIMOIfZ6uXRnZCcDTCw+Xvv025vsi9z3sZwAAcIzD3eG6deummjVrau7cufLxMR9+//59tWrVSl27dtXmzZufOkzk0aRUqVLFOk9oaKhCQ0PttyNHpAsLC1NYWNhTr/tpbNpk+/8ucDEzDOnECWnjxvsqW/YxlRI8VuQ2m9DbLtwH+xk8K/YzcBTbDBzhattLXHPYDONxxzGiS5o0qXbt2qV8+fJFmb53714VK1ZMt2/fdmRxdhEREapZs6auXr2qX375Jdb5hgwZoqFDh0abvnjxYgUEBDzVup/W5s2ZNWFCsSfO1737Dr366qkESAQgsWE/AwBA3N2+fVuNGzfWtWvXFBQUFOt8Dh8JCgoK0vHjx6MVQSdOnFBgYKDjSf9fhw4d9Pfffz+2AJKkfv36qXv37vbb169fV0hIiCpXrvzYPzQ+JEtm04QJT56vatUXVLZskfgPBLcTFham9evXq1KlSvL19bU6DlwQ+xk8K/YzcBTbDBzhattLXK9b6nAR9NZbb6lly5YaN26cSpYsKUnasmWLevXqpUaNGjm6OElSx44dtWrVKm3evFlZsmR57Lz+/v7y9/ePNt3X1zfBn/jy5c3RmU6divm8IJvNvL98eR+GscVjWbH9wj2wn4GzsJ+Bo9hm4AhX2V7imsHhImjcuHGy2Wx69913df/+ffvK2rVrp9GjRzu0LMMw1KlTJ61YsUI//fSTcuTI4WgcS3l7m8PTvvmm+UHk4Q8okdeRnTSJ63gAeHqP289EYj8DAIBjHB4dzs/PT5MnT9aVK1e0e/du7d69W5cvX9bEiRNjPELzOB06dNCnn36qxYsXKzAwUGfPntXZs2d1584dR2NZpm5d82KGmTNHnZ4lizmd63cAeFax7WckKXt2qUaNBI8EAIBbe6rrBElSQECAUqRIoRQpUjz1gAQzZ87UtWvXVK5cOWXMmNH+8+WXXz5tLEvUrSsdPSqtX39f3bvv0Pr193XkCAUQAOd5dD/z5Zf3lTKldOSINGqU1ekAAHAvDhdB9+/f18CBAxUcHKzs2bMre/bsCg4O1oABAxweGs8wjBh/mjVr5mgsy3l7S2XLGnr11VMqW9agawoAp3t4P1OnjqHp083pw4dLu3dbGg0AALficBHUqVMnzZkzR2PHjtWuXbu0a9cujR07VvPnz1fnzp3jIyMAIAYNG5pHiO7fl5o2le7dszoRAADuweGBERYvXqwvvvhCVatWtU8rXLiwQkJC1KhRI82cOdOpAQEAMbPZpJkzpc2bpb/+kkaOlGK4jBoAAHiEw0eC/P39lT179mjTc+TIIT8/P2dkAgDEUbp00owZZnvkSGnnTmvzAADgDhwugjp27Kjhw4crNDTUPi00NFQjR45Ux44dnRoOAPBk9eubP+HhZre4h3bPAAAgBg53h9u1a5d+/PFHZcmSRUWKmFcn//PPP3Xv3j1VqFBBdR8aEm358uXOSwoAiNX06dJPP0l//y0NG2YeFQIAADFzuAhKkSKF6tWrF2VaSEiI0wIBAByXNq15ftCbb0qjR0u1a0svvWR1KgAAXJPDRdDChQvjIwcA4BnVqyc1aiR9/rnUrJn0xx9SkiRWpwIAwPU89cVSAQCuZ+pUKX16ae9eacgQq9MAAOCaKIIAIBFJnVqaPdtsf/ihtG2btXkAAHBFFEEAkMjUqiW9844UEWF2i7tzx+pEAAC4FoogAEiEJk+WMmaUDhyQBg2yOg0AAK7FKUXQ1atXnbEYAICTpEolzZljtsePl3791do8AAC4EoeLoDFjxujLL7+0327QoIFSp06tzJkz688//3RqOADA03vjDfPiqYZhdou7fdvqRAAAuAaHi6BZs2bZrwu0fv16rV+/XmvWrFHVqlXVq1cvpwcEADy9SZOkTJmkgwel99+3Og0AAK7B4SLo7Nmz9iJo1apVatCggSpXrqzevXtr+/btTg8IAHh6KVJI8+aZ7cmTpZ9/tjQOAAAuweEiKGXKlDpx4oQkae3atapYsaIkyTAMhYeHOzcdAOCZVa0qtWxpdotr3ly6dcvqRAAAWMvhIqhu3bpq3LixKlWqpEuXLqlq1aqSpF27dil37txODwgAeHbjx0shIdKhQ1K/flanAQDAWg4XQRMnTlTHjh1VoEABrV+/XsmTJ5cknTlzRu3bt3d6QADAswsOftAtbupU6aefLI0DAIClfBx9gK+vr3r27Blterdu3ZwSCAAQPypXltq0MYfObt5c2rNH+v/vsQAA8CgOF0GR9u7dq+PHj+vevXtRptesWfOZQwEA4se4cdK6ddLRo1KfPtL06VYnAgAg4TlcBB0+fFh16tTRnj17ZLPZZBiGJMlms0kSgyMAgAsLDJTmz5cqVpRmzJDq1pUqVLA6FQAACcvhc4K6dOmiHDly6Pz58woICNA///yjzZs3q1ixYvqJTuYA4PIqVJDatTPbLVpI169bmwcAgITmcBG0detWDRs2TGnSpJGXl5e8vLxUunRpjRo1Sp07d46PjAAAJxs7VsqeXTp+XOI61wAAT+NwERQeHq7AwEBJUpo0aXT69GlJUrZs2XTgwAHnpgMAxIvkyaWFC832nDnS999bmwcAgITkcBFUqFAh/fnnn5Kk4sWLa+zYsdqyZYuGDRumnDlzOj0gACB+lCsndepktlu1kq5dszQOAAAJxuEiaMCAAYqIiJAkDRs2TEeOHFGZMmW0evVqTZkyxekBAQDxZ9QoKVcu6cQJqUcPq9MAAJAwHB4drkqVKvZ27ty5tX//fl2+fFkpU6a0jxAHAHAPyZKZ3eLKljVHjatXT6pa1epUAADEL4ePBMUkVapUFEAA4KbKlJG6dDHbrVpJV69aGgcAgHgXpyNBdevWjfMCly9f/tRhAADWGDlS+u476eBBqVu3B4MmAACQGMXpSFBwcLD9JygoSD/++KN27Nhhv/+PP/7Qjz/+qODg4HgLCgCIPwEB0qJFks1m/l61yupEAADEnzgdCVr40FeCffr0UYMGDTRr1ix5e3tLMofNbt++vYKCguInJQAg3pUsKXXvLo0fL7VpI/39t5QqldWpAABwPofPCVqwYIF69uxpL4AkydvbW927d9eCBQucGg4AkLCGD5fy5pXOnHlwnhAAAImNw0XQ/fv3tX///mjT9+/fbx86GwDgnpImNbvDeXlJn34qffON1YkAAHA+h4fIbt68uVq2bKlDhw7p5ZdfliT99ttvGj16tJo3b+70gACAhPXKK1KvXtKYMVLbtlLp0lLq1FanAgDAeRwugsaNG6cMGTJo/PjxOnPmjCQpY8aM6tWrl3pwpT0ASBSGDJG+/Vbau1fq1ElavNjqRAAAOI/D3eG8vLzUu3dvnTp1SlevXtXVq1d16tQp9e7dO8p5QgAA95Ukidktzttb+vxzadkyqxMBAOA8z3Sx1KCgIEaEA4BE6qWXpD59zHa7dtKFC9bmAQDAWRzuDidJX331lZYsWaLjx4/r3r17Ue7buXOnU4IBAKw3aJC0cqU5XHbHjtKXX1qdCACAZ+fwkaApU6aoefPmSp8+vXbt2qWXX35ZqVOn1uHDh1W1atX4yAgAsIi/v/TRR2a3uCVLzB8AANydw0XQjBkzNGfOHE2dOlV+fn7q3bu31q9fr86dO+vatWvxkREAYKH//U/q399st28vnTtnbR4AAJ6Vw0XQ8ePHVbJkSUlS0qRJdePGDUlSkyZN9Pnnnzs3HQDAJQwYIBUuLF26ZJ4fZBhWJwIA4Ok5XARlyJBBly9fliRlzZpV27ZtkyQdOXJEBu+KAJAo+fmZ3eJ8fKQVK6QvvrA6EQAAT8/hIui1117TypUrJZkXTu3WrZsqVaqkt956S3Xq1HF6QACAa3jhBWngQLPdsaN09qylcQAAeGoOjw43Z84cRURESJI6dOig1KlT69dff1XNmjXVtm1bpwcEALiOfv2kr7+Wdu2S3nvPPCpks1mdCgAAxzhcBHl5ecnL68EBpIYNG6phw4ZODQUAcE2+vma3uKJFpW++kT77THrnHatTAQDgmKe6TtDVq1f1+++/6/z58/ajQpHeffddpwQDALim55+XBg82B0vo1El67TUpUyarUwEAEHcOF0Hffvut3n77bd28eVNBQUGyPdQPwmazUQQBgAfo08fsCvfHH1LbtuYFVekWBwBwFw4PjNCjRw+1aNFCN2/e1NWrV3XlyhX7T+SocQCAxM3Hx+wW5+cnrVolffyx1YkAAIg7h4ugU6dOqXPnzgoICIiPPAAAN1GwoDR0qNnu0kU6edLaPAAAxJXDRVCVKlW0Y8eO+MgCAHAzPXtKL78sXbsmtW7NRVQBAO4hTucERV4XSJKqV6+uXr16ae/evXr++efl6+sbZd6aNWs6NyEAwGX5+EiLFkkvviitXSstWCC1bGl1KgAAHi9ORVDt2rWjTRs2bFi0aTabTeHh4c8cCgDgPvLnl0aMkHr1krp3lypVkrJmtToVAACxi1N3uIiIiDj9UAABgGfq1k0qUUK6fl1q1YpucQAA1+bwOUEAADzK29vsFpckibR+vTR3rtWJAACIXZy6w02ZMiXOC+zcufNThwEAuK/nnpM++MDsEtejh1S5spQ9u9WpAACILk5F0MSJE+O0MJvNRhEEAB6sc2dp+XLpl1/MARLWr5e86HMAAHAxcSqCjhw5Et85AACJgLe3tHChVLiwtGGDNHu21K6d1akAAIjqqb+fu3jxoi5evOjMLACARCB3bmn0aLPdq5d0+LC1eQAAeJRDRdDVq1fVoUMHpUmTRunTp1f69OmVJk0adezYUVevXo2niAAAd9Oxo/Tqq9KtW1KLFlJEhNWJAAB4IE7d4STp8uXLKlGihE6dOqW3335b+fPnlyTt3btXixYt0o8//qhff/1VKVOmjLewAAD34OX1oFvcpk3S9OlSp05WpwIAwBTnImjYsGHy8/PToUOHlD59+mj3Va5cWcOGDYvzIAoAgMQtZ05p7FipQwepb1+palWzqxwAAFaLc3e4r7/+WuPGjYtWAElShgwZNHbsWK1YscKp4QAA7u2996TXXpNu35aaN6dbHADANcS5CDpz5owKFiwY6/2FChXS2bNnnRIKAJA4eHlJ8+dLyZObw2Y7cNk5AADiTZyLoDRp0ujo0aOx3n/kyBGlSpXKGZkAAIlI9uzSuHFmu18/6d9/LY0DAEDci6AqVaro/fff171796LdFxoaqoEDB+r11193ajgAQOLQpo1UsaJ0967ZLS483OpEAABP5tDACMWKFVOePHnUoUMH5cuXT4ZhaN++fZoxY4ZCQ0P1ySefxGdWAICbstnMbnGFCkm//ipNmiT16GF1KgCAp4pzEZQlSxZt3bpV7du3V79+/WQYhiTJZrOpUqVKmjZtmkJCQuItKADAvWXNKk2YILVuLb3/vlS9upQvn9WpAACeKM5FkCTlyJFDa9as0ZUrV3Tw4EFJUu7cuTkXCAAQJy1bSl99Ja1bJzVtKm3ZIvk49E4EAMCzi/M5QQ9LmTKlXn75Zb388ssUQACAOLPZpHnzpOBg6fffpfHjrU4EAPBET1UEAQDwtLJkMc8JkqRBg6S9ey2NAwDwQBRBAIAE17SpeU7QvXtm+/59qxMBADwJRRAAIMHZbNLs2VKKFNKOHdLYsVYnAgB4EoogAIAlMmeWpkwx20OGSHv2WBoHAOBBKIIAAJZ55x2pZk0pLExq1sz8DQBAfKMIAgBYJrJbXKpU0s6d0ujRVicCAHgCiiAAgKUyZJCmTjXbw4ZJu3dbGgcA4AEoggAAlmvUSKpTxxwlrlkzc9Q4AADiC0UQAMByNps0c6aUOrX055/SyJFWJwIAJGYUQQAAl5A+vTRjhtn+4APzHCEAAOIDRRAAwGU0aCC9+eaDbnGhoVYnAgAkRhRBAACXMmOGlDated2g4cOtTgMASIwoggAALiVtWvP8IMkcMnvHDmvzAAASH4ogAIDLqVdPathQCg+XmjalWxwAwLkoggAALmnaNHOwhL17pSFDrE4DAEhMKIIAAC4pdWpp1iyzPXas9Ntv1uYBACQeFEEAAJdVu7b09ttSRIQ5Wtzdu1YnAgAkBhRBAACXNmWKlCGDtH+/NGiQ1WkAAIkBRRAAwKWlSiXNmWO2x42Tfv3V2jwAAPdHEQQAcHk1akjvvisZhtkt7vZtqxMBANwZRRAAwC1MmiRlyiQdPCgNGGB1GgCAO6MIAgC4hZQppblzzfakSdLPP1saBwDgxiiCAABuo1o1qUULs1tcixbSrVtWJwIAuCOKIACAW5kwQcqSRfrvP6l/f6vTAADcEUUQAMCtBAdL8+aZ7SlTpE2brM0DAHA/FEEAALdTpYrUurXZbt5cunnT2jwAAPdCEQQAcEvjxklZs0pHjkh9+1qdBgDgTiiCAABuKShImj/fbE+fLm3YYG0eAID7oAgCALitihWl994z2y1aSDduWJsHAOAeKIIAAG5t7Fgpe3bp2DGpVy+r0wAA3AFFEADArQUGSgsWmO3Zs6X1663NAwBwfRRBAAC3V7681LGj2W7ZUrp+3do8AADXRhEEAEgURo+WcuaUTpyQevSwOg0AwJVRBAEAEoVkyaSFC832vHnS2rXW5gEAuC6KIABAovHqq1KXLma7VSvp6lVL4wAAXBRFEAAgUfngAyl3bunUKal7d6vTAABcEUUQACBRCQiQFi2SbDaze9x331mdCADgaiiCAACJTqlSUrduZrt1a+nKFWvzAABcC0UQACBRGjFCeu456cyZB+cJAQAgUQQBABKppEmljz6SvLykTz6RVq60OhEAwFVQBAEAEq1XXpF69jTbbdtKly5ZmwcA4BooggAAidrQoVL+/NLZs1LnzlanAQC4AoogAECiliSJOVqcl5e0eLG0fLnViQAAVqMIAgAkei+/LPXpY7bbtZMuXrQ2DwDAWhRBAACPMHiwVLCgdP681LGj1WkAAFaiCAIAeAR/f3O0OG9v6csvpaVLrU4EALAKRRAAwGMULSr162e227c3jwoBADwPRRAAwKMMHCgVLmyeF9S+vWQYVicCACQ0iiAAgEfx8zNHi/PxkZYtM7vGAQA8C0UQAMDjvPiiNGCA2e7QwbyGEADAc1AEAQA8Uv/+0gsvSJcvS++9R7c4APAkFEEAAI/k62uOFufrK33zjXkhVQCAZ6AIAgB4rMKFpUGDzHanTtKZM9bmAQAkDIogAIBH69PHHDr7yhWpbVu6xQGAJ6AIAgB4NF9fc7Q4Pz/p22+lTz6xOhEAIL5RBAEAPF6hQtKQIWa7c2fp1ClL4wAA4hlFEAAAknr1kl56Sbp2TWrdmm5xAJCYUQQBACDz4qmLFkn+/tKaNdLChVYnAgDEF4ogAAD+X4EC0vDhZrtbN+nECWvzAADiB0UQAAAP6d5deuUV6fp1qVUrusUBQGJEEQQAwEO8vc1ucUmSSN9/L82bZ3UiAICzUQQBAPCIvHmlkSPNdvfu0rFj1uYBADgXRRAAADHo0kUqVUq6eVNq2ZJucQCQmFAEAQAQA29vc4S4pEmlH3+UZs+2OhEAwFkoggAAiEWePNKoUWa7Z0/pyBFr8wAAnIMiCACAx+jUSSpTRrp1S2rRQoqIsDoRAOBZUQQBAPAYXl5mt7iAAOmnn6QZM6xOBAB4VhRBAAA8Qa5c0tixZrtPH+nQIWvzAACeDUUQAABx0K6dVK6cdPu21Lw53eIAwJ1RBAEAEAdeXtKCBVKyZNLPP0tTp1qdCADwtCiCAACIoxw5pHHjzHa/ftLBg9bmAQA8HYogAAAc0LatVLGidOeO2S0uPNzqRAAAR1EEAQDgAJtNmjdPCgyUtmyRJk+2OhEAwFEUQQAAOChbNmn8eLP9/vvS/v3W5gEAOIYiCACAp9CqlVS5snT3rtSsGd3iAMCdUAQBAPAUIrvFBQVJv/324MgQAMD1UQQBAPCUQkKkSZPM9qBB0t69lsYBAMQRRRAAAM+gWTOpWjUpNNRs379vdSIAwJNQBAEA8AxsNmnOHCk4WNq+XfrwQ6sTAQCehCIIAIBnlDmzNGWK2R48WPr7b2vzAAAejyIIAAAnaNJEqlFDCgszu8WFhVmdCAAQG4ogAACcwGaTZs+WUqaU/vhDGjPG6kQAgNhQBAEA4CQZM0pTp5rtYcOkP/+0Ng8AIGYUQQAAOFHjxlLt2g+6xd27Z3UiAMCjKIIAAHAim02aNUtKnVravVv64AOrEwEAHkURBACAk6VPL02fbrZHjpR27bI2DwAgKoogAADiQYMGUr165sVTmzalWxwAuBKKIAAA4oHNJs2YIaVJI+3ZIw0fbnUiAEAkiiAAAOJJunRmISRJo0ZJO3ZYmwcAYKIIAgAgHtWvL731lhQebo4WFxpqdSIAAEUQAADxbNo086jQP/9IQ4danQYAQBEEAEA8S5PGHDZbksaMkX7/3do8AODpKIIAAEgAdeqYF1KNiDBHi7t71+pEAOC5KIIAAEggU6ZIGTJI+/dLgwZZnQYAPBdFEAAACSR1amn2bLM9fry0dau1eQDAU1EEAQCQgGrWlJo0MbvFNWsm3bljdSIA8DwUQQAAJLDJk6WMGaV//5UGDLA6DQB4HoogAAASWMqU0ty5ZnviROmXX6zNAwCehiIIAAALVK8uNW8uGYb5+/ZtqxMBgOegCAIAwCITJkhZskj//Sf17291GgDwHBRBAABYJEUKad48sz15srRpk6VxAMBjUAQBAGChKlWkVq3MdosW0s2b1uYBAE9AEQQAgMXGj5dCQqTDh6W+fa1OAwCJH0UQAAAWCwqSFiww29OnSxs3WpsHABI7iiAAAFxAxYpS27Zmu0UL6cYNa/MAQGJGEQQAgIv48EMpWzbp6FGpd2+r0wBA4kURBACAiwgMfNAtbtYs6YcfrM0DAIkVRRAAAC7ktdekDh3MdsuW0vXr1uYBgMSIIggAABczerSUM6d0/LjUs6fVaQAg8aEIAgDAxSRP/qBb3Ny50rp11uYBgMSGIggAABdUtqzUubPZbtlSunrV0jgAkKhQBAEA4KI++EDKnVs6dUrq3t3qNACQeFAEAQDgopIlkxYulGw28/fq1VYnAoDEgSIIAAAXVrq01LWr2W7dWrpyxdI4AJAoUAQBAODiRoyQnntOOn36QUEEAHh6FEEAALi4gABp0SLJy0v6+GPp22+tTgQA7o0iCAAAN1CihNSjh9lu00a6fNnaPADgziiCAABwE8OGSfnySWfPPhg+GwDgOIogAADcRJIk0kcfmd3iPvtMWrHC6kQA4J4oggAAcCMvvyz17m2233tPunjR2jwA4I4oggAAcDNDhkgFC0rnz0sdO1qdBgDcD0UQAABuxt/fHC3O21v68kvpq6+sTgQA7oUiCAAAN1SsmNS3r9lu1848KgQAiBuKIAAA3NTAgdLzz5vnBbVvLxmG1YkAwD1QBAEA4KYiu8X5+EjLlklLllidCADcA0UQAABu7H//k95/32x36CCdO2dtHgBwBxRBAAC4uf79pRdekC5dMs8PolscADweRRAAAG7Oz+9Bt7gVK6TPP7c6EQC4NoogAAASgSJFpEGDzHbHjtKZM9bmAQBXRhEEAEAi0beveY7QlStS27bS/fvSpk02bd6cWZs22RQebnVCuLrwcLYZxJ07by+WF0GbN29WjRo1lClTJtlsNn399ddWRwIAwC35+koffWT+/vZbKX16qVIlH02YUEyVKvkoe3Zp+XKrU8JVLV8uZc/ONoO4cfftxfIi6NatWypSpIimT59udRQAANxeoUJS/fpm+/LlqPedOiW9+ab7fEhBwlm+3Nw2Tp6MOp1tBjFJDNuL5UVQ1apVNWLECNWpU8fqKAAAuL3wcGnz5pjvixw1rmtXuVW3FcSv8HCpS5eYRxVkm8GjEsv24mN1AEeFhoYqNDTUfvv69euSpLCwMIWFhVkVy57h4d/Ak7DNwFFsM3iSTZtsOnky9rd3w5BOnJBy5zaUPHkCBoPLunlTOnnSFuv9bDN4WFy3l40b76ts2YQfrz+u749uVwSNGjVKQ4cOjTb9+++/V0BAgAWJolu/fr3VEeBm2GbgKLYZxGbz5sySij1xvqNHY/8QA8SEbQaOWLNmt27dOpXg6719+3ac5rMZhutcUs1ms2nFihWqXbt2rPPEdCQoJCREFy9eVFBQUAKkjF1YWJjWr1+vSpUqydfX19IscA9sM3AU2wyeZNMmmypVevJ3nGPGhKtwYZf5CAAL/fWXTX36eD9xPrYZSHHfXtavt+ZI0PXr15UmTRpdu3btsbWB2x0J8vf3l7+/f7Tpvr6+LvOBwJWywD2wzcBRbDOITfnyUpYs5gnKMX3NabOZ9/fo4S3vJ3+OgQeoVEmaOpVtBnET1+2lfHkfS7aXuL43Wj4wAgAAcB5vb2nyZLNte6T3UuTtSZPEh1nYsc3AEYlle7G8CLp586Z2796t3bt3S5KOHDmi3bt36/jx49YGAwDATdWtK331lZQ5c9TpWbKY0+vWtSYXXBfbDByRGLYXy7vD7dixQ+XLl7ff7t69uySpadOmWrRokUWpAABwb3XrSrVqmSM0rVmzW1WrvmBZ9xS4B7YZOMLdtxfLi6By5crJhcZmAAAg0fD2lsqWNXTr1imVLVvEbT6cwDpsM3CEO28vlneHAwAAAICERBEEAAAAwKNQBAEAAADwKBRBAAAAADwKRRAAAAAAj0IRBAAAAMCjUAQBAAAA8CgUQQAAAAA8CkUQAAAAAI9CEQQAAADAo1AEAQAAAPAoFEEAAAAAPApFEAAAAACP4mN1gGdlGIYk6fr16xYnkcLCwnT79m1dv35dvr6+VseBG2CbgaPYZuAothk4im0GjnC17SWyJoisEWLj9kXQjRs3JEkhISEWJwEAAADgCm7cuKHg4OBY77cZTyqTXFxERIROnz6twMBA2Ww2S7Ncv35dISEhOnHihIKCgizNAvfANgNHsc3AUWwzcBTbDBzhatuLYRi6ceOGMmXKJC+v2M/8cfsjQV5eXsqSJYvVMaIICgpyiY0A7oNtBo5im4Gj2GbgKLYZOMKVtpfHHQGKxMAIAAAAADwKRRAAAAAAj0IR5ET+/v4aPHiw/P39rY4CN8E2A0exzcBRbDNwFNsMHOGu24vbD4wAAAAAAI7gSBAAAAAAj0IRBAAAAMCjUAQBAAAA8CgUQQAAAAA8CkUQAAAAAI9CEeQEmzdvVo0aNZQpUybZbDZ9/fXXVkeCCxs1apReeuklBQYGKl26dKpdu7YOHDhgdSy4sJkzZ6pw4cL2q3GXKFFCa9assToW3Mjo0aNls9nUtWtXq6PARQ0ZMkQ2my3KT758+ayOBRd36tQpvfPOO0qdOrWSJk2q559/Xjt27LA6VpxQBDnBrVu3VKRIEU2fPt3qKHADmzZtUocOHbRt2zatX79eYWFhqly5sm7dumV1NLioLFmyaPTo0frjjz+0Y8cOvfbaa6pVq5b++ecfq6PBDWzfvl2zZ89W4cKFrY4CF1ewYEGdOXPG/vPLL79YHQku7MqVKypVqpR8fX21Zs0a7d27V+PHj1fKlCmtjhYnPlYHSAyqVq2qqlWrWh0DbmLt2rVRbi9atEjp0qXTH3/8oVdffdWiVHBlNWrUiHJ75MiRmjlzprZt26aCBQtalAru4ObNm3r77bc1d+5cjRgxwuo4cHE+Pj7KkCGD1THgJsaMGaOQkBAtXLjQPi1HjhwWJnIMR4IAi127dk2SlCpVKouTwB2Eh4friy++0K1bt1SiRAmr48DFdejQQdWrV1fFihWtjgI3cPDgQWXKlEk5c+bU22+/rePHj1sdCS5s5cqVKlasmOrXr6906dLpxRdf1Ny5c62OFWccCQIsFBERoa5du6pUqVIqVKiQ1XHgwvbs2aMSJUro7t27Sp48uVasWKECBQpYHQsu7IsvvtDOnTu1fft2q6PADRQvXlyLFi1S3rx5debMGQ0dOlRlypTR33//rcDAQKvjwQUdPnxYM2fOVPfu3dW/f39t375dnTt3lp+fn5o2bWp1vCeiCAIs1KFDB/3999/0u8YT5c2bV7t379a1a9f01VdfqWnTptq0aROFEGJ04sQJdenSRevXr1eSJEmsjgM38HC3/sKFC6t48eLKli2blixZopYtW1qYDK4qIiJCxYoV0wcffCBJevHFF/X3339r1qxZblEE0R0OsEjHjh21atUqbdy4UVmyZLE6Dlycn5+fcufOraJFi2rUqFEqUqSIJk+ebHUsuKg//vhD58+f1//+9z/5+PjIx8dHmzZt0pQpU+Tj46Pw8HCrI8LFpUiRQs8995z+++8/q6PARWXMmDHaF3H58+d3m26UHAkCEphhGOrUqZNWrFihn376ya1OIoTriIiIUGhoqNUx4KIqVKigPXv2RJnWvHlz5cuXT3369JG3t7dFyeAubt68qUOHDqlJkyZWR4GLKlWqVLRLfPz777/Kli2bRYkcQxHkBDdv3ozyTcmRI0e0e/dupUqVSlmzZrUwGVxRhw4dtHjxYn3zzTcKDAzU2bNnJUnBwcFKmjSpxengivr166eqVasqa9asunHjhhYvXqyffvpJ69atszoaXFRgYGC08wyTJUum1KlTc/4hYtSzZ0/VqFFD2bJl0+nTpzV48GB5e3urUaNGVkeDi+rWrZtKliypDz74QA0aNNDvv/+uOXPmaM6cOVZHixOKICfYsWOHypcvb7/dvXt3SVLTpk21aNEii1LBVc2cOVOSVK5cuSjTFy5cqGbNmiV8ILi88+fP691339WZM2cUHByswoULa926dapUqZLV0QAkEidPnlSjRo106dIlpU2bVqVLl9a2bduUNm1aq6PBRb300ktasWKF+vXrp2HDhilHjhyaNGmS3n77baujxYnNMAzD6hAAAAAAkFAYGAEAAACAR6EIAgAAAOBRKIIAAAAAeBSKIAAAAAAehSIIAAAAgEehCAIAAADgUSiCAAAAAHgUiiAAQKKwY8cOTZw4UREREVZHAQC4OIogAIDLOHr0qGw2m3bv3u3Q4y5cuKD69eurUKFC8vJ6/Ftbs2bNVLt2bfvtcuXKqWvXro6HBQC4LYogAIDTNGvWTDabLdrP66+/HqfHh4SE6MyZMypUqFCc1xkREaEmTZpo8ODBqlSpksOZly9fruHDhzv8OACA+/KxOgAAIHF5/fXXtXDhwijT/P394/RYb29vZciQwaH1eXl5ae3atQ495mGpUqV66scCANwTR4IAAE7l7++vDBkyRPlJmTKlJMlms2nmzJmqWrWqkiZNqpw5c+qrr76yP/bR7nBXrlzR22+/rbRp0ypp0qTKkydPlAJrz549eu2115Q0aVKlTp1abdq00c2bN+33h4eHq3v37kqRIoVSp06t3r17yzCMKHkf7Q535coVvfvuu0qZMqUCAgJUtWpVHTx40H7/sWPHVKNGDaVMmVLJkiVTwYIFtXr1amc+hQCAeEYRBABIUAMHDlS9evX0559/6u2331bDhg21b9++WOfdu3ev1qxZo3379mnmzJlKkyaNJOnWrVuqUqWKUqZMqe3bt2vp0qX64Ycf1LFjR/vjx48fr0WLFmnBggX65ZdfdPnyZa1YseKx+Zo1a6YdO3Zo5cqV2rp1qwzDULVq1RQWFiZJ6tChg0JDQ7V582bt2bNHY8aMUfLkyZ307AAAEgLd4QAATrVq1apoRUH//v3Vv39/SVL9+vXVqlUrSdLw4cO1fv16TZ06VTNmzIi2rOPHj+vFF19UsWLFJEnZs2e337d48WLdvXtXH3/8sZIlSyZJmjZtmmrUqKExY8Yoffr0mjRpkvr166e6detKkmbNmqV169bFmv3gwYNauXKltmzZopIlS0qSPvvsM4WEhOjrr79W/fr1dfz4cdWrV0/PP/+8JClnzpxP8zQBACxEEQQAcKry5ctr5syZUaY9fN5NiRIlotxXokSJWEeDa9eunerVq6edO3eqcuXKql27tr042bdvn4oUKWIvgCSpVKlSioiI0IEDB5QkSRKdOXNGxYsXt9/v4+OjYsWKResSF2nfvn3y8fGJ8pjUqVMrb9689qNVnTt3Vrt27fT999+rYsWKqlevngoXLhyHZwYA4CroDgcAcKpkyZIpd+7cUX6edvCBqlWr6tixY+rWrZtOnz6tChUqqGfPnk5O7JhWrVrp8OHDatKkifbs2aNixYpp6tSplmYCADiGIggAkKC2bdsW7Xb+/PljnT9t2rRq2rSpPv30U02aNElz5syRJOXPn19//vmnbt26ZZ93y5Yt8vLyUt68eRUcHKyMGTPqt99+s99///59/fHHH7GuK3/+/Lp//36Ux1y6dEkHDhxQgQIF7NNCQkL03nvvafny5erRo4fmzp0b9ycAAGA5usMBAJwqNDRUZ8+ejTLNx8fHPqDB0qVLVaxYMZUuXVqfffaZfv/9d82fPz/GZQ0aNEhFixZVwYIFFRoaqlWrVtkLprfffluDBw9W06ZNNWTIEF24cEGdOnVSkyZNlD59eklSly5dNHr0aOXJk0f58uXThAkTdPXq1Viz58mTR7Vq1VLr1q01e/ZsBQYGqm/fvsqcObNq1aolSeratauqVq2q5557TleuXNHGjRsfW8QBAFwPRRAAwKnWrl2rjBkzRpmWN29e7d+/X5I0dOhQffHFF2rfvr0yZsyozz//PMpRlof5+fmpX79+Onr0qJImTaoyZcroiy++kCQFBARo3bp16tKli1566SUFBASoXr16mjBhgv3xPXr00JkzZ9S0aVN5eXmpRYsWqlOnjq5duxZr/oULF6pLly564403dO/ePb366qtavXq1fH19JZnDbnfo0EEnT55UUFCQXn/9dU2cOPGZnjMAQMKyGbGdHQoAgJPZbDatWLFCtWvXtjoKAMCDcU4QAAAAAI9CEQQAAADAo3BOEAAgwdADGwDgCjgSBAAAAMCjUAQBAAAA8CgUQQAAAAA8CkUQAAAAAI9CEQQAAADAo1AEAQAAAPAoFEEAAAAAPApFEAAAAACP8n//4Tr4DoPfPAAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    }
  ]
}