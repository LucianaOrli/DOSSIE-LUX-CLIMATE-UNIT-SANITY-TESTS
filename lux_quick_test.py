class LuxEngine:
    def check(self, temps):
        return 'ONDA DE CALOR' if len([t for t in temps if t >= 35]) >= 5 else 'Normal'

e = LuxEngine()
res = e.check([35, 35, 35, 35, 35])
print(f'\n[LUX CLIMATE] STATUS: {res} ✅')

