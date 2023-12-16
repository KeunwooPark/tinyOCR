from src.dataloader.TextDataLoader import TextDataLoader
import pathlib


class ArxivDataLoader(TextDataLoader):
    def __init__(self):
        super().__init__()
        self.root = pathlib.Path(__file__).parent.parent.parent / "dataset"

    def load_text_items(self) -> dict:
        titles, abstracts = self._load_csv()
        return titles + abstracts

    def _load_csv(self):
        csv_path = self.root / "arxiv_data.csv"

        titles = []
        abstracts = []
        with open(csv_path, "r") as f:
            content = f.read()
            items = content.split(",")
            # the first three items are the headers
            items = items[3:]

            for i, item in enumerate(items):
                if i % 3 == 0:
                    titles.append(item)
                else:
                    abstracts.append(item)

        return titles, abstracts
