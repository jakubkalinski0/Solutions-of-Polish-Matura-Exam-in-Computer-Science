# Solutions of Polish Matura Exam in Computer Science

Zbiór rozwiązań zadań z egzaminu maturalnego z informatyki (poziom podstawowy i rozszerzony). Repozytorium obejmuje zadania programistyczne, bazodanowe oraz arkuszowe z lat 2005–2023.

## Struktura repozytorium

| Katalog | Opis | Liczba zadań |
|---------|------|--------------|
| [`coding_tasks/`](coding_tasks/) | Zadania programistyczne w Pythonie | 47 |
| [`database_tasks/`](database_tasks/) | Bazy danych Access (`.accdb`) wraz z plikami źródłowymi | 36 |
| [`excel_tasks/`](excel_tasks/) | Arkusze kalkulacyjne Excel (`.xlsx`) i odpowiedzi | 13 |

Każde zadanie znajduje się w osobnym katalogu. Nazwa folderu ma postać:

```
<prefix>_<rok>_<nazwa_zadania>
```

### Prefiksy nazw

| Prefiks | Znaczenie |
|---------|-----------|
| `mp_` | Matura podstawowa |
| `mr_sf_` | Matura rozszerzona — stara formuła (do 2014) |
| `mr_nf_` | Matura rozszerzona — nowa formuła (od 2015) |
| `mr_nf_dod_` | Zadania dodatkowe (nowa formuła) |
| `mr_prob_` / `mr_nf_prob_` | Zadania próbne |

## Zadania programistyczne (`coding_tasks/`)

Rozwiązania napisane w Pythonie. Typowa struktura katalogu:

- `1.py`, `2.py`, … — rozwiązania poszczególnych podpunktów zadania
- `dane.txt`, `przyklad.txt` — dane wejściowe z arkusza egzaminacyjnego
- `wyniki*.txt` — wygenerowane odpowiedzi

Aby uruchomić rozwiązanie, przejdź do katalogu zadania i wykonaj:

```bash
python 1.py
```

> Skrypty zakładają, że pliki danych znajdują się w tym samym katalogu co program.

## Zadania bazodanowe (`database_tasks/`)

Zawierają bazy Microsoft Access (`.accdb`) oraz pliki tekstowe z danymi źródłowymi (`.txt`). Bazy można otworzyć w Microsoft Access lub kompatybilnym oprogramowaniu i wykonać zapytania SQL zgodnie z treścią zadania maturalnego.

## Zadania arkuszowe (`excel_tasks/`)

Zawierają arkusze Excel (`.xlsx`) wraz z plikami tekstowymi z odpowiedziami do podpunktów teoretycznych. Arkusze wymagają Microsoft Excel lub kompatybilnego edytora arkuszy kalkulacyjnych.

## Licencja

Projekt udostępniony na licencji [MIT](LICENSE).

## Autor

Jakub Kaliński
