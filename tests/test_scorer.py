from app.services.scorer import score_resume

def test_score_contains_detected_role():
    text = "Data Scientist with Python, pandas, SQL"
    result = score_resume(text)
    assert "detected_role" in result

def test_score_range_valid():
    text = "DevOps engineer with Docker and AWS"
    result = score_resume(text)
    assert 0 <= result["score"] <= 100

def test_missing_keywords_present():
    text = "Python developer"
    result = score_resume(text)
    assert len(result["missing_keywords"]) > 0
