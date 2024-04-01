context = """
You are a specialized assistant whose role is to meticulously analyze news articles, with a keen focus on thematic pillars that encompass constraints on government powers, governance, transparency, corruption, freedom, human rights, equality, justice, and civic participation. Your task consists in, first, reading a news article and preparing a concise summary that underscores its relevance to a specific thematic pillar and, second, provide an evaluation on how the events narrated by the article impact the thematic pillar specified. I will provide you with further details about the news articles and the chosen pillar.
"""

instructions = """
Given the following news article:
News title: {headline}
News summary: {summary}
News body: {body}
Thematic pillar: This news article is related to the {pillar_name} pillar, which emcompasses the following items:
{pillar_bullets}

Use the following JSON format to answer:
{{
    "summary": "A concise, professional summary of the news article, highlighting its relevance to the specified pillar. Include important places, events, and details specific to the pillar it is associated with.",
    "impact_score": "A value from 1 to 5, where 1 means that the news article has a strong negative impact on the thematic pillar and 5 means that the news article has a strong positive impact on the thematic pillar. Following the same reasoning, a value of 3 means that the events have a neutral impact on the thematic pillar"
}}

The summary should clearly articulate how the news article's content relates to the specified thematic pillar. It should be very concise and professional, including crucial places, events, and relevant details. The main topic of the news article should be evident in the summary, without omitting any essential details. Additionally, you should take everything from the news article into account, such as events, places, people, etc. and use this information to determine how negative or positive is the impact of the news article on the specified pillar.

Remember to ONLY answer following the JSON format provided and using double quotes. Only give the answer in the JSON format and refrain from additional comments or explanations.
"""

pillar_names = {
    "1": "Constraints of Government Powers",
    "2": "Absence of corruption",
    "3": "Open Government",
    "4": "Fundamental Freedoms",
    "5": "Order and Security",
    "6": "Regulatory Enforcement",
    "7": "Civil Justice",
    "8": "Criminal Justice"
}

pillar_bullets = {
    "1": """
    - The active and reactive transparency of legislative bodies (senate, parliament, assemblies), its ability to impose disciplinary measures to government officials, and if there is representation of disadvantaged groups, as well as citizen participation. It also measures if the opposition can express its opinions and if it exercises its functions of overseeing and investigating the government.
    - The independence of the judiciary, by means of having sufficient resources and professional judges, with adequate rights and competencies, as well as its ability to impose disciplinary measures on government officials.
    - The independence and effectiveness of oversight institutions, such as the Supreme Audit Institution or comptroller, anticorruption authority, human rights institution, the office of the ombudsman, and prosecution services, as well as if civil servants are free from political pressure, and are effective in implementing public policies.
    - Whether elections are free of barriers of entry, intimidation, corruption, and criminality, in accordance with the law, with equitable access to resources, free from misinformation, secure from cyberattacks and with protection of personal. It also measures the effectiveness and independence of the electoral authority.
    - The effectiveness of non-governmental checks on the government’s power, such as the media, CSOs, political parties, activists, and citizens. It includes their effective exercise of the freedoms of assembly, association, opinion, and expression, and the rights to petition and civic engagement.
    - The accountability of the Chief Executive or the Head of Government, and its respect for the constitutional order, the law-making process, the outcome and quality of elections, civil liberties, political opponents, as well as the independence of the judiciary and oversight institutions. It also measures the likelihood of sanctions to officials for misconduct.
    - Whether members of the legislature, judiciary, elected leaders or high-ranking government officials, public sector employees, and police officers, who abuse their power are sanctioned for misconduct.
    """,
    
    "2": """
    - The prevalence of bribery in the delivery of public services and regulations, as well as in the political process. 
    - The prevalence of graft by elected officials, public sector employees, by awarding contracts without competitive bidding processes, exerting influence for their private benefit, and using insider knowledge to profit.
    - The prevalence of embezzlement or misappropriation of public funds, payroll fraud, asset misappropriation and skimming, as well as of nepotism, favoritism, and patronage.
    - The prevalence of nepotism and favoritism by elected officials, public sector employees, judges, and prosecutors. It also measures the prevalence of patronage by elected officials.
    - The prevalence of corruption in elections, including illegal campaign financing, manipulation of elections, and vote buying. 
    """,
    
    "3": """
    - Whether requests for information from the public to government agencies and institutions are granted, and if these requests are granted within a reasonable time period, with complete and pertinent answers, at a reasonable cost and without having to pay a bribe for the information.
    - Whether people are aware of their right to information, and whether relevant records are accessible to the public upon request.
    - The effectiveness of non-governmental checks on the government's power, as well as the openness of the civic space and the extent of citizen participation. It includes the effective exercise of the freedoms of assembly, association, opinion, and expression, and the rights to petition and civic engagement. 
    """,
    
    "4": """
    - The protection of rights related to dignity, including the prohibition of torture, slavery and forced labor.  
    - The protection of rights related to freedom, including freedom of thought, conscience, religion, peaceful assembly, association, opinion, and expression, as well as the right to property and to asylum.
    - Whether civil society organizations are free to comment on government policies, without fear of retaliation. In addition, it also measures if quarantines and lockdowns are applied proportionately, not discriminatory, with limited duration and in accordance with the law.
    - Whether independent media, civil society organizations, members of the opposition, opposing factions of the governing party, activists, whistleblowers, and individuals are free to report and comment on government policies, without fear of retaliation.
    - The extent to which the media publish credible fact-checked information, and if its editorial content is independent from political influences, as well as if it can conduct investigations and expose cases of corruption without facing surveillance, harassment, threats, legal actions, or administrative sanctions.
    - The extent to which the government allows the formation or operation of CSOs, and the formation or operation of opposition parties.
    - Whether the government respects the property rights of people and corporations, refrains from the illegal seizure of private property, and provides adequate reasons and compensation when property is legally expropriated. It also measures if the process for transferring a property is simple and quick. In addition, it measures if foreign investors receive fair and equitable treatment from the government, and the effective enforcement of anti-squatting laws and intellectual property rights.
    - Whether the government respects the right to asylum and refugees can move freely within the host country, have access to legal work and state services such as education, accommodation, meals, healthcare, and cash benefits, as well as legal documentation and economic opportunities.
    - The protection of rights related to equality, including equality before the law, and absence of discrimination based on socio-economic status, gender, ethnicity, religion, national origin, sexual orientation, or gender identity.
    - The protection of rights related to solidarity, including labor rights such as workers’ right to information, consultation, collective bargaining, access to placement services, and protection in the event of unjustified dismissal, as well as the prohibition of child labor.
    - The protection of rights related to citizens´ rights, including political rights such as the right to vote and to stand as a candidate at European Parliament and municipal elections, to information, petition, movement, and of residence.
    - The protection of rights related to justice, including the right to effective remedy and to a fair trial, presumption of innocence, and to defense, as well as rights of the accused including principles of legality and proportionality of criminal offenses and penalties, and the right not to be tried or punished twice. 
    """,
    
    "5": """
    - The extent to which people feel safe and secure in their city, town, or village, and in their neighborhood.
    - The extent to which the State is able to keep crime and violence to minimum levels. 
    """,
    
    "6": """
    - The extent to which the legal framework for businesses is clear, accessible, and predictable, as well as the respect for property rights.
    - Whether the government respects the property rights of people and corporations, refrains from the illegal seizure of private property, and provides adequate reasons and compensation when property is legally expropriated. In addition, it measures if foreign investors receive fair and equitable treatment from the government, and the effective enforcement of anti-squatting laws and intellectual property rights. 
    - Whether the process for transferring a property is simple and quick. 
    - The extent to which the government audits and inspections are conducted in accordance with the law and are free of corruption; if complaint mechanisms are simple, accessible, and cost-effective, and if regulation authorities are impartial, and if they sanction violations.
    - Whether environmental and labor regulation authorities sanction violations, such as occupational safety and business license or zoning violations. 
    """,
    
    "7": """
    - Whether justice institutions help prevent legal and justice needs. It also measures whether authorities tolerate illegal activities such as squatting, street vending or informal labor arrangements.
    - Whether people are aware of their rights, formal justice, and alternative justice mechanisms, and know where to get information and advice when facing a legal problem.
    - Whether people can access and afford legal advice and representation; and can access the court system without incurring unreasonable fees.
    - Whether the civil justice system is impartial and free of discrimination, corruption and undue influence from the government and private interests.
    - The effectiveness and timeliness of the enforcement of civil justice decisions and judgments in practice.
    - Whether alternative dispute resolution mechanisms (ADRs) are available, accessible, affordable, impartial, timely, effective, enforceable, and free of corruption and undue influence from the government and private interests. 
    """,
    
    "8": """
    - Whether criminal investigations are effective, timely, impartial, and free of corruption and undue influence from criminal organizations and political and private interests.
    - The effectiveness of prosecutors in investigating crimes, and if pre-trial proceedings are timely, outcome-oriented, impartial, and free of corruption and undue influence from political and private interests.
    - Whether trials are timely, outcome-oriented, impartial, and free of corruption and undue influence from political and private interests.
    - Whether alternative dispute resolution mechanisms (ADRs) are available, accessible, affordable, impartial, timely, effective, enforceable, and free of corruption and undue influence from the government and private interests.
    - Whether victim's rights are effectively guaranteed, including treatment with respect, absence of discrimination, timely and sufficient information, and protection.
    - Whether the basic rights of criminal suspects are respected, including the presumption of innocence and the freedom from arbitrary arrest and unreasonable pre-trial detention. It also measures whether criminal suspects are able to access and challenge evidence used against them, whether they are subject to abusive treatment, and whether they are provided with adequate legal assistance. In addition, it measures whether the basic rights of prisoners are respected once they have been convicted of a crime.
    - Whether the prison system guarantees conditions of safety and order and respects the rights of people deprived of their liberty. It also measures the absence of corruption and the effectiveness of the prison system in reducing recidivism. 
    """
}

pillar_summary_prompt = """
You are a specialized assistant whose role is to meticulously read and analyze a list of summaries from news articles and provide a list of the most important events related to a specific topic. The thematic topics encompass constraints on government powers, governance, transparency, corruption, freedom, human rights, equality, justice, and civic participation. I will provide you with further details about the news articles and the specific topic.

We will now work with the {pillar_name} topic, which encompasses the following aspects:
{pillar_bullets}

The individual articles that we have at hand are the following:
{summaries}

Use the following JSON format to answer:
{{
    "list_of_events": "A list of bullet points summarizing the most relevant events or issues narrated by the individual articles."
}}

Important things to take into account when performing this task:
- Feel free to group multiple articles into a single issue if they are related.
- Do not make any reference to the articles in your answer.
- The description of each event or issue should be no more than 25 words.
- I would like to have a maximum of FIVE events and/or issues listed, no more. Please use the topic issues provided above to identify the most relevant events.
- Remember to ONLY answer following the JSON format provided and using double quotes. 
- Only give the answer in the JSON format and refrain from additional comments or explanations.
"""

pillar_summary_context = """
You are a specialized assistant whose role is to meticulously read and analyze a list of summaries that were extracted from news articles and provide a list of the most important events related to a specific topic.  I will provide you with further details about the news article summaries and the specific topic that I would like you to focus on. You will have to carefully read the information I will provide to you and identify the most relevant issues or events related to the thematic topic that I will specify. The topics that we will cover are related to constraints on government powers, governance, transparency, corruption, freedom, human rights, equality, justice, and civic participation. Therrefore, you will have to use your knowledge on politics, law, and social sciences to sucessfully perform this task.
"""

pillar_summary_instructions = """
We will now work with the {pillar_name} topic, which encompasses the following aspects:
{pillar_bullets}

The individual articles that we have at hand are the following:
{summaries}

Taking into account the topic and article summaries that I provided above, please come up with a list of the TEN most relevant events or issues covered in the articles. Please use the topic aspects to determine how relevant is each one of the events or issues that you identified in the summaries.

Use the following JSON format to answer:
{{
    "list_of_events": "A list of bullet points summarizing the TEN most relevant events or issues narrated by the individual articles."
}}

When performing this task, please take into account the following things:
- I would like to have a maximum of TEN events and/or issues listed, no more. Please use the topic aspects provided above to identify the most relevant issues or events.
- Feel free to group multiple articles depending on the issue that they are covering.
- The description of each event or issue should be no more than 30 words.
- Remember to ONLY answer following the JSON format provided and using double quotes. Only give the answer in the JSON format and refrain from additional comments or explanations.
"""