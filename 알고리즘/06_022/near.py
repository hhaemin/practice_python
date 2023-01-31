class Top5Players:

    def __init__(self, cs, ns):
        self.currentScores = cs
        self.newScore = ns

    def setAlignScore(self):
        nearIdx = 0
        nearScore = 0
        minNum = 10.0

        for i, s in enumerate(self.currentScores):
            absNum = abs(self.newScore - s)

            if absNum < minNum:
                minNum = absNum
                nearIdx = i
                nearScore = s

        # print(f'nearIdx: {nearIdx}')
        # print(f'nearScore: {nearScore}')

        if self.newScore >= self.currentScores[nearIdx]:
            for i in range(len(self.currentScores)-1, nearIdx, -1):
                self.currentScores[i] = self.currentScores[i-1]

            self.currentScores[nearIdx] = self.newScore

        else:
            for i in range(len(self.currentScores)-1, nearIdx+1, -1):
                self.currentScores[i] = self.currentScores[i-1]

            self.currentScores[nearIdx+1] = self.newScore

        # print(f'self.currentScores: {self.currentScores}')

    def getFinalTop5Scores(self):
        return self.currentScores