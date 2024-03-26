from os.path import join, dirname


async def get_files(filename):
    return join(dirname(__file__), filename)
