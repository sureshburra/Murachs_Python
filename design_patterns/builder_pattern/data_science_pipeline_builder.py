class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, data):
        for step in self.steps:
            data = step(data)
        return data


class PipelineBuilder:
    def __init__(self):
        self._steps = []

    def add_step(self, step):
        self._steps.append(step)
        return self

    def add_normalization(self):
        def normalize(data):
            mn, mx = min(data), max(data)
            return [(x - mn) / (mx - mn) for x in data]

        self._steps.append(normalize)
        return self

    def add_threshold_filter(self, threshold):
        def filt(data):
            return [x for x in data if x >= threshold]

        self._steps.append(filt)
        return self

    def build(self):
        return Pipeline(self._steps)


# Usage
pipeline = PipelineBuilder().add_normalization().add_threshold_filter(0.5).build()

result = pipeline.run([1, 2, 3, 4, 5])
print(result)
