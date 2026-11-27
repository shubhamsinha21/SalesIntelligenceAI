## SalesIntel AI is an AI-powered Sales Research Multi-agent system that automatically researches companies and generated detailed sales intelligence reports.

Example - a sales person wants to approach stripe, Instead of manually searching the internet, he enternet stripe into the application. The company collects info, products, key people and potential sales opportunities.

## Multi-agent sales research system with Treg, langgraph, Guardrails and Fast API.

## Supervisor agent (team manager)
(controls the flow, choosed next ageny, stops when all tasks are done)
- Web research agent
- company intelligence agent
- people research agent
- report writer agent

## Results into final sales research report
- (company overview, products, people, opportunites, sources)

## Guardrails
1. input validation
2. website validation
3. evidence filtering
4. citation validation
5. cost control
6. execution control

## Treg API Key
- (Unified data and tools layer) -> One API Key
1. web search (treg.web.search) -> find comany and news
2. website scrapping (treg.web.extract) -> extract website content
3. company data (company info via web search) -> busines, products, industry
4. people search (treg.people.search) -> find company professionals

## End to end workflow
1. user enters "company name"
2. agents collect data via Treg
3. open ai analyses and creates a sales research report
4. display the final report

## Guardrails do
- keep input safe and valid
- ensure trusted data resources
- remove sensitive info
- verify citations, sources
- control cost and execution

## Key components
1. Treg
2. Langgraph
3. Open AI
4. Fast API
5. HTML/CSS/JS

## How does it work

```
Users enters a company name (stripe)
        |
        Fast API Backend
        |
        Langgraph supervisor
        |
        Web research agent ------ Treg
        |
        Company intelligence ----- Treg
        |
        People research agent ----- Treg
        |
        Report writer agent ----- LLM
        | 
        Validation & Final report
        |
        User interface
```

## What is Treg ?
- An AI model can understand info and generate text. However, it needs external tools to collect up-to-date info from the internet.

- Treg enters here..

- Treg acts as a unified gateway bet our agents and external data providers.

- Without tregm we might need separate accounts, API keys and integrations for web search, website scrapping and people search.

- With treg, we can access with just one api key.

## Files and structure 
- main.py -> endpoints
- static -> script and css files
- templates -> index file
- graph.py 
- guardrails
- treg