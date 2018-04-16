describe("Hangman", function() {
    describe("Game Result", function() {
        it("should pass", function(){
            let guessResponse = {

                "win": true
            }
            expect(isGameWon(guessResponse)).toBe(true);
        });
    });

});