from text_factory.cleaning import clean_text

def test_clean_text():
    assert clean_text('  blabla  ') == 'blabla'
    assert clean_text('b   labla ') == 'b labla'
    assert clean_text(' B	labLa') == 'b labla'
    assert clean_text(' \n blabla') == 'blabla'
    assert clean_text('    ') == ''



