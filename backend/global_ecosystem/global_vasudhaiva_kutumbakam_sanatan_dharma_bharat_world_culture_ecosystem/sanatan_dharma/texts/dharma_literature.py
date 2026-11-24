"""Dharma literature map: distinguish genres, periods and normative claims."""
DHARMA_TEXT_GENRES = {
 "dharmasutra":{"description":"Early sutra-style works discussing dharma, conduct, social duties and ritual obligations.","examples":["Apastamba Dharmasutra","Gautama Dharmasutra","Baudhayana Dharmasutra","Vasistha Dharmasutra"],"caution":"Do not assume one text represents every region, period or community."},
 "dharmashastra":{"description":"Verse and prose normative literature on law, conduct, social order, penance and duties.","examples":["Manusmriti","Yajnavalkya Smriti","Narada Smriti","Parashara Smriti"],"caution":"These are historically situated normative texts, not a uniform description of what all people practised."},
 "nibandha":{"description":"Later digests and compilations that select, compare and interpret earlier authorities.","research_questions":["which authorities are cited","regional legal custom","commentarial disagreement","historical period"]},
 "commentary":{"description":"Interpretive traditions explaining, qualifying or disputing a root text.","research_questions":["commentator and lineage","date and region","textual recension","audience and purpose"]}
}
def list_dharma_genres():
    return {key:dict(value) for key,value in DHARMA_TEXT_GENRES.items()}
