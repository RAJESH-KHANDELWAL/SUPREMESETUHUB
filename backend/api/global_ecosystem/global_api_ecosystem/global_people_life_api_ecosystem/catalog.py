"""Canonical people, work and life taxonomy; classification only, not a live directory."""

DOMAINS = (
    {"id":"life-stages","name":"Human Life Stages & Situations","groups":["infants","children","teenagers","young adults","adults","older adults","senior citizens","parents","caregivers","retired people","career changers"]},
    {"id":"education-learning","name":"Education, Students & Lifelong Learning","groups":["schools","colleges","universities","vocational training","coaching","tutoring","online learning","scholarships","internships","apprenticeships"]},
    {"id":"jobs-careers","name":"Jobs, Careers & Occupations","groups":["government jobs","private jobs","international jobs","remote work","hybrid work","part-time","full-time","contract work","gig work","freelancing","recruitment","career transitions"]},
    {"id":"entrepreneurship","name":"Entrepreneurship & Self-Employment","groups":["solo founders","home businesses","family businesses","microbusinesses","small businesses","MSMEs","startups","scaleups","franchises","cooperatives","social enterprises","investors","incubators"]},
    {"id":"households-care","name":"Households, Homemaking, Parenting & Care","groups":["homemakers","household management","parenting","childcare","elder care","caregiving","domestic services","single-parent households","multigenerational households"]},
    {"id":"gender-inclusion","name":"Gender, Inclusion & Equal Opportunity","groups":["women and girls","men and boys","gender-diverse people","disability inclusion","accessible services","equal opportunity","inclusive education","inclusive workplaces"]},
    {"id":"relationships","name":"Friendship, Dating, Relationships & Family Life","groups":["friendship","dating","romance","couples communication","marriage preparation","marriage support","relationship education","couples counselling","family counselling","co-parenting"]},
    {"id":"sexual-health-intimacy","name":"Sexual Health, Intimacy & Adult Education","groups":["sexual health education","reproductive health","consent education","healthy intimacy","adult couples wellbeing","marital intimacy education","STI information and testing"],"adult_context":True},
    {"id":"adult-media-18-plus","name":"Lawful Adult Media & Entertainment (18+)","groups":["adult films","adult video platforms","adult media publishing","adult creator platforms","adult studios","adult content moderation","performer safety"],"adult_only":True,"minimum_age":18,"safeguards":["verified adults only","documented informed consent","no coercion or exploitation","no non-consensual imagery","jurisdiction-specific legal review","privacy and age controls"]},
    {"id":"adult-couple-services-18-plus","name":"Consensual Adult Couple Intimacy Services (18+)","groups":["adult couples education","marital intimacy education","premarital sexual-health education","couples wellbeing counselling"],"adult_only":True,"minimum_age":18,"safeguards":["adults only","freely given ongoing consent","professional boundaries","privacy","local legal compliance"]},
    {"id":"family-safeguarding","name":"Family Safety, Child Protection & Survivor Support","groups":["child protection","abuse prevention","family violence support","survivor services","trauma-informed counselling","emergency referrals"],"safeguards":["separate from adult entertainment","protect children and vulnerable people","prioritise survivor safety"]},
    {"id":"coaching-consulting","name":"Coaching, Consulting, Mentoring & Advisory","groups":["business coaching","career coaching","leadership coaching","life coaching","relationship coaching","management consulting","technology consulting","qualified legal and tax advisory"]},
    {"id":"health-wellbeing","name":"Health, Wellbeing & Personal Development","groups":["primary healthcare","specialist care","mental health","fitness","nutrition","preventive health","rehabilitation","disability support","personal development"]},
    {"id":"daily-needs","name":"Daily Needs, Consumer Services & Local Trades","groups":["food","groceries","clothing","housing","utilities","transport","personal care","repairs","cleaning","laundry","shopping","delivery"]},
    {"id":"finance-livelihood","name":"Personal Finance, Livelihood & Economic Participation","groups":["financial literacy","budgeting","banking access","payments","credit education","insurance","tax education","retirement planning","grants and benefits"]},
    {"id":"culture-community","name":"Culture, Faith, Recreation & Community","groups":["arts","music","books","sports","hobbies","heritage","faith communities","volunteering","charities","events","travel"]},
    {"id":"digital-creators","name":"Digital Life, Creators & Online Communities","groups":["bloggers","video creators","podcasters","streamers","influencers","online educators","affiliate publishers","marketplaces","social networks","online safety"]},
    {"id":"civic-public-services","name":"Civic Life, Legal Information & Public Services","groups":["citizen services","civil documentation","legal information","legal aid","consumer rights","labour rights","business licensing","immigration information","social protection","emergency services"]},
    {"id":"housing-property","name":"Housing, Property & Construction","groups":["renting","home ownership","real estate","property management","construction","renovation","home safety","housing support"]},
    {"id":"mobility-global-locations","name":"Global Locations, Migration & Mobility","groups":["countries","states and provinces","cities","districts","neighbourhoods","rural communities","relocation","study abroad","work abroad","migration information","cross-border services"]},
)

FACETS = {
    "age_bands":["early_childhood","child","teen","18_24","25_34","35_44","45_54","55_64","65_plus"],
    "life_situations":["student","job_seeker","employee","self_employed","entrepreneur","homemaker","parent","caregiver","retired","career_changer"],
    "work_modes":["employee","freelance","gig","contract","internship","apprenticeship","self_employed","business_owner","volunteer"],
    "delivery_channels":["online","offline","hybrid"],
    "organization_sizes":["individual","home_based","micro","small","medium","large","enterprise","multinational"],
    "gender_inclusion":["women_and_girls","men_and_boys","gender_diverse","all_genders","not_specified"],
    "location_levels":["global","country","state_or_province","city","district","neighbourhood","rural_locality"],
}
