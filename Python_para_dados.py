{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN5dWj5wg35bf3EZXUaoINS",
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
        "<a href=\"https://colab.research.google.com/github/JuniaBS/Estudando-An-lise-de-Dados/blob/main/Python_para_dados.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "zIWa2tQAiF5x"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Python para Dados - Atividade de Fixação Numpy"
      ],
      "metadata": {
        "id": "XQpeQr2TiULh"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1 - Explorando Ecossistemas:\n",
        "Como bióloga marinha, me encontrei em uma expedição nas\n",
        "profundezas do Oceano Pacífico, onde estávamos estudando a\n",
        "biodiversidade e a saúde dos recifes de coral. O catálogo abaixo\n",
        "demonstra dados das espécies encontradas, considere a seguinte\n",
        "ordem de colunas:"
      ],
      "metadata": {
        "id": "XhdPPiRPik8s"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "ID da espécie, quantidade de representantes encontrados, profundeza,\n",
        "tamanho médio da espécie.\n",
        "a. Selecione a segunda coluna com a quantidade de espécies\n",
        "encontradas e adicione em um array as qtd_especies.\n",
        "b. De qtd_especies selecione apenas as primeiras 3 quantidades e\n",
        "print.\n",
        "c. Print as 5 últimas quantidades de espécies.\n",
        "d. Crie um array que contenha apenas os tamanhos das espécies e\n",
        "ordene por ordem crescente."
      ],
      "metadata": {
        "id": "oZzntsq8irbK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np"
      ],
      "metadata": {
        "id": "Dl6LaYw1jEht"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "especies = np.array([[747, 89, 33, 5],\n",
        "[623, 123, 32, 13],\n",
        "[501, 22, 49, 2],\n",
        "[116, 101, 42, 10],\n",
        "[297, 56, 69, 22],\n",
        "[613, 64, 27, 7],\n",
        "[295, 84, 29, 14],\n",
        "[692, 105, 72, 16],\n",
        "[229, 103, 35, 5],\n",
        "[374, 124, 70, 1]])"
      ],
      "metadata": {
        "id": "Q3Nk9s4OifbZ"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Selecione a segunda coluna com a quantidade de espécies\n",
        "encontradas e adicione em um array as qtd_especies."
      ],
      "metadata": {
        "id": "Ki6JAWCsje8h"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "qtd_especies = especies[:,1]\n",
        "qtd_especies"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u9KnREnojepa",
        "outputId": "fefdc908-9d4b-4b83-ccd5-f78a426acf48"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([ 89, 123,  22, 101,  56,  64,  84, 105, 103, 124])"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "De qtd_especies selecione apenas as primeiras 3 quantidades e\n",
        "print."
      ],
      "metadata": {
        "id": "ugTGb9Q6kDA4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(qtd_especies[:3])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rFSoF8SbkIkN",
        "outputId": "9b81cd0d-eabe-4ed3-e5df-a1103a80e9ec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[ 89 123  22]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Print as 5 últimas quantidades de espécies."
      ],
      "metadata": {
        "id": "15_T8bUhkqwZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "qtd_especies[-5:]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3jp6l_tbkuEq",
        "outputId": "253a382b-24d2-4181-d8ca-09d30fc6e44d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([ 64,  84, 105, 103, 124])"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Crie um array que contenha apenas os tamanhos das espécies e\n",
        "ordene por ordem crescente."
      ],
      "metadata": {
        "id": "0ApGrIfjkxG7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "np.sort(especies[:,3])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "idEBgFxOlBab",
        "outputId": "69fbe5fc-c3b4-45a3-a9ff-62a946f2700f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([ 1,  2,  5,  5,  7, 10, 13, 14, 16, 22])"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 2. Ainda usando o Array de espécies marítimas."
      ],
      "metadata": {
        "id": "t_WHRjDu-Y5q"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Usando um index boolean crie um array que contém os dados da\n",
        "maior espécie encontrada (considerando o seu tamanho), esse\n",
        "valor corresponde ao valor 22."
      ],
      "metadata": {
        "id": "IAnmUNoM-cYq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "maior_especie = especies[especies[:,3] == 22]\n",
        "maior_especie"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ThtCCQvKBu0V",
        "outputId": "2baa8177-a98a-4527-d5f4-dc082a6efed9"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[297,  56,  69,  22]])"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Usando fency index faça um array que contém apenas dados da\n",
        "espécie com ID 297."
      ],
      "metadata": {
        "id": "JFLT3T5g-j9m"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "mask_297 = especies[:,0] == 297"
      ],
      "metadata": {
        "id": "DuTJ-KYc-ksM"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "especies[mask_297]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nq7ELUBHClkB",
        "outputId": "9cdc4351-e164-4660-e95f-9fe23bf994b8"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[297,  56,  69,  22]])"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Usando np.where() faça um array com a linha com dados\n",
        "correspondentes a espécie com 105 representantes\n",
        "encontrados."
      ],
      "metadata": {
        "id": "GcPdsFTz-lXR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "np.where(especies[:,1] == 105)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2BZspMFb-oYj",
        "outputId": "abef137d-6f81-4d0a-f941-78561eac1199"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(array([7]),)"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "especies[np.where(especies[:,1] == 105)]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q5RSEK0hDLst",
        "outputId": "3bf10441-1e05-4e06-a557-0c39ca8a7f97"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[692, 105,  72,  16]])"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Considere a profundeza em que o espécie foi encontrada\n",
        "substitua valores maiores que 60 com \"Profundo”"
      ],
      "metadata": {
        "id": "zG8r-anD-o-P"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "especies[:,2]>60"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uJYW-B8k-rGE",
        "outputId": "e6047a75-b82b-41b3-b3df-fbb532e66293"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([False, False, False, False,  True, False, False,  True, False,\n",
              "        True])"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "especies[:,2]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NVnipH-bD79S",
        "outputId": "d139d511-195a-45da-fa1f-e58babcb1cf5"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([33, 32, 49, 42, 69, 27, 29, 72, 35, 70])"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "np.where(especies[:,2]>60, \"Profundo\", especies[:,2])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UVbLcOAyDf0B",
        "outputId": "a59e3172-bbeb-4aed-af8c-448ee684ffc8"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['33', '32', '49', '42', 'Profundo', '27', '29', 'Profundo', '35',\n",
              "       'Profundo'], dtype='<U21')"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 3. Ainda no conjunto 'especies'."
      ],
      "metadata": {
        "id": "OIo1ed1nIAXQ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Adicione mais 2 espécies ao array: [[204, 10, 40, 12], [392, 11, 81,\n",
        "11]]."
      ],
      "metadata": {
        "id": "aenCLz39NsRX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "especies"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TN2WMs13OzvQ",
        "outputId": "ee3ee47d-ec17-45f0-fc14-258ea351d84c"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[747,  89,  33,   5],\n",
              "       [623, 123,  32,  13],\n",
              "       [501,  22,  49,   2],\n",
              "       [116, 101,  42,  10],\n",
              "       [297,  56,  69,  22],\n",
              "       [613,  64,  27,   7],\n",
              "       [295,  84,  29,  14],\n",
              "       [692, 105,  72,  16],\n",
              "       [229, 103,  35,   5],\n",
              "       [374, 124,  70,   1]])"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "novas_especies = np.array ([[204, 10, 40, 12], [392, 11, 81, 11]])"
      ],
      "metadata": {
        "id": "Nb8evRkHNv4s"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "np.concatenate((especies, novas_especies))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AQIuyRxIOSVE",
        "outputId": "4e2a5f55-ca02-4a90-e002-096a9d7434bb"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[747,  89,  33,   5],\n",
              "       [623, 123,  32,  13],\n",
              "       [501,  22,  49,   2],\n",
              "       [116, 101,  42,  10],\n",
              "       [297,  56,  69,  22],\n",
              "       [613,  64,  27,   7],\n",
              "       [295,  84,  29,  14],\n",
              "       [692, 105,  72,  16],\n",
              "       [229, 103,  35,   5],\n",
              "       [374, 124,  70,   1],\n",
              "       [204,  10,  40,  12],\n",
              "       [392,  11,  81,  11]])"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Adicione mais uma coluna na no array original agora com o\n",
        "número de espécies encontradas com que indica se o animal\n",
        "enxerga ou não: [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0]."
      ],
      "metadata": {
        "id": "9JzzkoZtNxMQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ver = np.array([0, 1, 0, 0, 0, 0, 1, 0, 1, 1]).reshape((10,1))\n",
        "ver"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m2i_IirNQZXR",
        "outputId": "54250e7b-b4fc-4251-b7f2-86f077e90896"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0],\n",
              "       [1],\n",
              "       [0],\n",
              "       [0],\n",
              "       [0],\n",
              "       [0],\n",
              "       [1],\n",
              "       [0],\n",
              "       [1],\n",
              "       [1]])"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "np.concatenate((especies, ver), axis=1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "obnmQnJbNzM6",
        "outputId": "092f0f1f-0338-40ad-fd3c-179b51d5e3be"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[747,  89,  33,   5,   0],\n",
              "       [623, 123,  32,  13,   1],\n",
              "       [501,  22,  49,   2,   0],\n",
              "       [116, 101,  42,  10,   0],\n",
              "       [297,  56,  69,  22,   0],\n",
              "       [613,  64,  27,   7,   0],\n",
              "       [295,  84,  29,  14,   1],\n",
              "       [692, 105,  72,  16,   0],\n",
              "       [229, 103,  35,   5,   1],\n",
              "       [374, 124,  70,   1,   1]])"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "3UJYPMyRPU29"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "wamy4Io-NvIp"
      }
    }
  ]
}