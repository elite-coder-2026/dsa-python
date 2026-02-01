from sortedcontainers import SortedDict

class EventScheduler:
    def __init__(self):
        self.evt = SortedDict()

    def schedule(self, ts, evt):
        self.evt[ts] = evt

    def get_evts_in_range(self, start, end):
        result = []

        for ts in self.evt.irange(start, end):
            result.append((ts, self.evt[ts]))

        return result

    def next_evt_after(self, ts):
