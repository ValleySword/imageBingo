from .interfaces.images_search_condition import ImagesSearchCondition

def parse_json_file(file):
    return [
        ImagesSearchCondition(
            id=idx,
            name=t["name"],
            keywords=t["keywords"],
            success=t["success"],
            error=t["error"],
        ) for idx, t in enumerate(file)
    ]
