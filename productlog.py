
class ProductLog:

    def __init__(self, file_path):
        pass

if __name__ == '__main__':

    p = ProductLog('/foo/bar/com/log.txt')
    errors = p.errors
    summary_stats = p.get_summary_stats()


