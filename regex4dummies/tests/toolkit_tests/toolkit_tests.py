class ToolkiTests:

    def __init__( self, *args, **kwargs ):
        """
        Blank constructor method
        """

        pass


    def run_tests( self, tool_tester ):
        """
        Runs tests, then returns
        """

        # Clearing screen
        print "Toolkit Tests: "
        print "---------------"
        print ""

        # Testing NLTK functions
        print "NLTK Toolkit tests:"
        # tokenizer function
        print tool_tester.tokenize( "This is a test string.", "nltk" )
        # dependency function
        print tool_tester.find_dependencies( "This is a test string.", "nltk" )
        print ""

        # Testing Pattern functions
        print "Pattern Toolkit tests:"
        # tokenizer function
        print tool_tester.tokenize( "This is a test string.", "pattern" )
        # dependency function
        print tool_tester.find_dependencies( "This is a test string.", "pattern" )
        print ""

        # Testing Nlpnet functions
        print "Nlpnet Toolkit tests:"
        # tokenizer function
        print tool_tester.tokenize( "This is a test string.", "nlpnet" )
        # dependency function
        print tool_tester.find_dependencies( "This is a test string.", "nlpnet" )
        print ""

        # Testing general functions
        print "General Toolkit tests:"
        # tokenizer function
        print "Tokenized average: " + str( tool_tester.tokenize( "This is a test string.", "" ) )
        print "Noun Phrases: " + str( tool_tester.extract_noun_phrases( "This is a test string." ) )
        print "Verb Phrases: " + str( tool_tester.extract_verb_phrases( "This is a test string." ) )
        print "Prepositional Phrases: " + str( tool_tester.extract_prepositional_phrases( "This is a test string in the house." ) )
        print ""

        # Clearing screen
        print ""
