"""
Prompt to run qa (English). Replace the text and question and play around!
"""
prompt = """Answer only based on the information in each text.
###
Text: When Russia invaded Ukraine a year ago, one of the biggest successes they achieved initially was in southern Ukraine. Within a few days Russian troops attacking from Crimea had seized an area of Ukrainian territory bigger than Switzerland.
Ukrainian authorities are yet to explain what went wrong in the south in those early days. To help uncover what happened, the BBC has spoken to military officers, politicians and activists.
On 22 February 2022 at 19:15, the secretary of Ukraine's security council Oleksiy Danilov received a red folder with secret documents. They warned that the president's life was under imminent threat. Immediately, Mr Danilov contacted the head of the security services, the interior minister, prime minister and President Volodymyr Zelensky himself.
Question: How large was the territory that Russia had conquered?
Answer: In a matter of days, the Russian troops, launching an offensive from Crimea, swiftly captured a territory exceeding the size of Switzerland.
###
Text: The largest economies in South America by GDP are Brazil, Argentina, Colombia, Peru, Chile, and Ecuador. Brazil has the largest economy in South America, with a GDP of approximately $2.4 trillion in 2021, driven by its manufacturing and service industries, as well as its vast natural resources, including oil and minerals. Argentina has the second-largest economy in South America, with a GDP of approximately $400 billion in 2021, driven by its agricultural exports, manufacturing, and services industries. Colombia has the third-largest economy in South America, with a GDP of approximately $335 billion in 2021, driven by its oil and gas production, mining, and manufacturing industries.
Question: What's the GDP of Argentina compared to the GDP of Colombia?
Answer: Argentina, with a GDP of approximately $400 billion in 2021, holds the position of the second largest economy in South America, while Colombia, with a GDP of $335 billion in the same year, trails behind. Consequently, Argentina's GDP surpasses Colombia's by approximately $65 billion.
###
Text: The Fourier Transform is a fundamental concept in mathematics that finds applications in many fields, including signal processing, quantum mechanics, and image analysis. It expresses a function as a sum of sinusoidal waves of different frequencies and amplitudes. The formula for the Fourier Transform of a function f(x) is given by:
F(ω) = ∫[from -∞ to ∞] f(x)e^(-iωx) dx
where F(ω) is the transformed function at frequency ω, e is the base of the natural logarithm, i is the imaginary unit, and the integral is taken over all values of x. Although the formula may seem complex, it enables researchers to analyze signals in the frequency domain and obtain useful information about their underlying properties.
Question: In what areas can the Fourier Transform be applied?
Answer: By utilizing the Fourier transform, researchers gain the capability to examine signals in the frequency domain and extract valuable insights pertaining to their fundamental characteristics. This transformative mathematical tool finds extensive utility in various domains such as signal processing, quantum mechanics, and image analysis.
###
Text: Good morning Lorenz,
perfect. In terms of content, we would like to stay with the questions that were originally planned.
From our side, seven people, including myself, will participate.
Also, we would still like to start at 11:00. I will send you the Webex meeting link in time. Would that fit for you?
Best regards
Til
Question: When will the meeting start and how many people will attend?
Answer: The meeting will be held via Webex. The proposed start time is 11:00 and seven people will attend.
###
Text: There are four pollination groups in apple trees, depending on climate:
Group A – Early flowering, 1 to 3 May in England ('Gravenstein', 'Red Astrachan')
Group B – 4 to 7 May ('Idared', 'McIntosh')
Group C – Mid-season flowering, 8 to 11 May ('Granny Smith', 'Cox's Orange Pippin')
Group D – Mid/late season flowering, 12 to 15 May ('Golden Delicious', 'Calville blanc d'hiver')
Question: When do Group D apple trees flower?
Answer: Apple tree varieties classified under Group D typically blossom during the middle to late period of the growing season, specifically from May 12 to 15. Notable examples of varieties within this group encompass 'Golden Delicious' and 'Calville blanc d'hiver'.
###
Text: {text}
Question: {question}
Answer:"""

settings = {
    "maximum_tokens": 128,
    "stop_sequences": ["###"]
}

model = "luminous-supreme"