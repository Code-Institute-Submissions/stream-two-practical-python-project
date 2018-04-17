describe("Hangman", function() {
    describe("Game Result", function() {
        it("should pass", function(){
            let guessResponse = {

                "win": true
            }
            expect(hangman.result(guessResponse)).toBe(true);
        });
    });

});