{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.7.6"
    },
    "colab": {
      "name": "1_a_Python.ipynb",
      "provenance": [],
      "toc_visible": true
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EduG0mqCgMdY",
        "colab_type": "text"
      },
      "source": [
        "# Exercise I: Your own Python module "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "W3BbD4XrgMdb",
        "colab_type": "code",
        "colab": {},
        "outputId": "711140f4-767b-40ec-86ab-518985e5274f"
      },
      "source": [
        "#check if notebook runs in colab\n",
        "import sys\n",
        "IN_COLAB = 'google.colab' in sys.modules\n",
        "print('running in Colab:',IN_COLAB)\n",
        "path='..'\n",
        "if IN_COLAB:\n",
        "  #in colab, we need to clone the data from the repo\n",
        "  !git clone https://github.com/keuperj/DataScienceSS20.git\n",
        "  path='DataScienceSS20'\n",
        "  import sys\n",
        "  sys.path.append(path+'/Exercises/')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "running in Colab: False\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lb2DIEacgMd-",
        "colab_type": "text"
      },
      "source": [
        "Write your own python module (choose a name) with the following properties:\n",
        "\n",
        "1. start new python file for the module\n",
        "2. define a class ***ListKeeper*** with the following properties and API:\n",
        "   1. ***Listkeeper*** strores named lists (hint: use dictionaries) \n",
        "   2. it initializes with a list named *example*: [1,2,3,4,5]\n",
        "   3. ``show()`` returns all list names\n",
        "   4. ``add(name, list)`` adds a new list\n",
        "   5. ``delete(name)`` deletes list\n",
        "   6. ``sort(name)`` returns the sorted list *name*\n",
        "   7. ``append(name, list)`` appends *list* to *name* \n",
        "3. add comments and documentation to your class\n",
        "4. Import your module in this notebook\n",
        "5. write tests to check the functionality of your class "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sa3vn2GjgMeK",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "8a2a8785-8f8e-410c-b80d-770b6e331d39"
      },
      "source": [
        "import ListKeeperModule\n",
        "\n",
        "lk = ListKeeperModule.ListKeeper()\n",
        "\n",
        "lk.add(\"animals\", [\"dog\", \"zebra\", \"cat\", \"mouse\", \"rabbit\"])\n",
        "\n",
        "lk.sort(\"animals\")\n",
        "\n",
        "lk.show()"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['example', 'animals']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    }
  ]
}