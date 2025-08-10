1. Der cleane, vom User geschriebene Code ist in `Raw.tl`
2. Anschließend wird der `preprocessor.py` ausgeführt, der Kommentare und unnötige Zeilen entfernt und diesen TimLang-Code unter `processed.tl` zu speichern
3. Der `compiler.py` liest den code aus `processed.tl` und wandelt ihn in `output.py` in ausführbaren Python-Code um
