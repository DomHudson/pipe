from concurrent.futures import ThreadPoolExecutor


class Pipe:

    def __init__(self, threads = 2, exception_handler = None, chunksize = 24, processor = None):
        """ Constructor.

        :return void
        """
        self.threads = threads
        self.chunksize = chunksize
        self.exceptionHandler = exceptionHandler
        self.processor = processor

    def run(self, items, work):
        """ Run the pipe. Multithread work in batches
        and yield results in the order they were submitted.

        :yield mixed
        """
        with ThreadPoolExecutor(max_workers = self.threads) as pool:
            
            chunk = []
            for item in items:

                chunk.append(pool.submit(work, item))

                if len(chunk) == self.chunksize:
                    yield from self._unchunk(chunk)
                    chunk = []

            if chunk:
                yield from self._unchunk(chunk)

    def _unchunk(self, chunk):
        """ Unchunk a list of future objects yielding
        them in order as the result comes in.
        
        :raises mixed 
        :yield mixed
        """
        for future in chunk:

            try:
                result = future.result()

                if callable(self.processor):
                    yield self.processor(result)
                else:
                    yield result

            except Exception as e:

                if not self.exception_handler:
                    raise e

                self.exception_handler(e)