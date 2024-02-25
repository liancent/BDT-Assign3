import json

class JsonReader():
    def __init__(self) -> None:
        pass

    def export_json_data(self, json_input, file_output):
        """
        Format and export the REST API response into a readable JSON file
        """
        with open(file_output, 'w', encoding='utf-8') as output:
            json.dump(json_input.json(), output, indent=4, sort_keys=True)

    # def retrieve_