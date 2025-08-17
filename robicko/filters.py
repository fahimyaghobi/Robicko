class filters:
    text = lambda msg: isinstance(msg, str)
    photo = lambda msg: hasattr(msg, "photo")
