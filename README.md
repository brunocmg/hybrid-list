# Hybrid List

An educational web application that demonstrates a **hybrid list**: a large sorted region searched with binary search, plus a small unsorted tail searched sequentially and merged into the sorted region once it fills up.

Built with **Python** and **Streamlit**.

> **Note:** the application interface is in Brazilian Portuguese.

## Features

- **Sorted region:** 1024 distinct integers generated from a fixed seed (`42`), so every run starts from the same data.
- **Unsorted tail:** new keys are appended to a tail with a limit of 10 elements.
- **Hybrid search:** binary search on the sorted region first, then sequential search on the tail.
- **Iteration counters:** each search reports binary iterations, sequential iterations and the total.
- **Automatic merge:** on the 10th insertion the tail is sorted and merged into the sorted region, and the tail is emptied.
- **Duplicate rejection:** a key already present in either region is not inserted.
- **State panel:** size of the sorted region, tail occupancy (with a progress bar) and number of merges performed.
- **Data viewer:** tabs listing the sorted region and the tail with their indexes.
- **Source viewer:** the code of the main methods is shown inside the app.
- **Reset:** restores the initial structure.

## How it works

| Operation | Behavior |
| --- | --- |
| Insert | Searches the whole structure first; if the key is new, appends it to the tail. When the tail reaches 10 keys, a merge is triggered. |
| Search | Binary search on the sorted region. If not found, sequential search on the tail. |
| Merge | Sorts the tail and merges it with the sorted region in a single pass (two pointers), then clears the tail. |

## Tech stack

- Python
- Streamlit
- pandas
- pytest

## Running locally

Requires Python 3.10 or newer.

```bash
git clone https://github.com/brunocmg/lista-hibrida.git
cd lista-hibrida
pip install -r requirements.txt
streamlit run app.py
```

## Tests

```bash
pytest
```

The tests cover the initial state, seed reproducibility, insertion, duplicate rejection, both search types, iteration counts and the automatic merge.

## Usage

1. In **Inserir uma chave**, type an integer and click **Inserir chave**.
2. In **Buscar uma chave**, type an integer and click **Buscar chave** to see where it was found, its index and how many iterations each search took.
3. Use the tabs under **Visualização das regiões** to inspect the sorted region and the tail.
4. Insert 10 new keys to see the tail being sorted and merged into the sorted region.
5. Click **Reiniciar estrutura** to start over.

## Project structure

```
.
├── app.py                  
├── lista_hibrida.py        
├── test_lista_hibrida.py   
└── requirements.txt        
```

## Author

- [Bruno Gomes](https://github.com/brunocmg)
- Alexandre Mascarenhas
