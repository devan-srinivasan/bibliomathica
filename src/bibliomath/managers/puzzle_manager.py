from bibliomath.models import Puzzle
from bibliomath.helper import jsonify_puzzle

class PuzzleManager:
    def __init__(self) -> None:
        pass

    def get_all_puzzles(self):
        return jsonify_puzzle(Puzzle.objects.all())

    def add_puzzle(self, puzzle):
        all_puzzles = self.get_all_puzzles()
        for puz in all_puzzles:
            if puzzle['question'] == puz['question'] or puzzle['title'] == puz['title']:
                return False
        new_puz = Puzzle(title=puzzle['title'], question=puzzle['question'], answer=puzzle['answer'])
        new_puz.save()
        return True

    def get_answer(self, title):
        ans_puz = Puzzle.objects.filter(title=title)
        return str(ans_puz.first().answer)