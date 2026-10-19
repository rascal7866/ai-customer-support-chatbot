# ChatCactus — AI Customer Support Platform & Educational Chatbot Project

[![Website](https://img.shields.io/badge/Website-ChatCactus-2ea44f)](https://chatcactus.com/)
[![Project](https://img.shields.io/badge/Project-Educational%20Demo-blue)](https://github.com/rascal7866/ai-customer-support-chatbot)

> Explore an educational AI customer support chatbot project inspired by **[ChatCactus](https://chatcactus.com/)**, an **[AI customer support platform](https://chatcactus.com/)** that helps businesses build knowledge-grounded AI agents and connect customer conversations across multiple channels.

**Website:** https://chatcactus.com/  
**Platform features:** https://chatcactus.com/features  
**Integrations:** https://chatcactus.com/integrations  
**API documentation:** https://chatcactus.com/docs

## Table of Contents

1. [Overview](#overview)
2. [About the Educational Repository](#about-the-educational-repository)
3. [About the ChatCactus Platform](#about-the-chatcactus-platform)
4. [Core Platform Capabilities](#core-platform-capabilities)
5. [Supported Communication Channels](#supported-communication-channels)
6. [How the Platform Works](#how-the-platform-works)
7. [Who Can Benefit](#who-can-benefit)
8. [Common Business Use Cases](#common-business-use-cases)
9. [Security, Privacy, and Administration](#security-privacy-and-administration)
10. [Developer API and Integrations](#developer-api-and-integrations)
11. [Plans and Getting Started](#plans-and-getting-started)
12. [Educational Project: Running and Testing](#educational-project-running-and-testing)
13. [Frequently Asked Questions](#frequently-asked-questions)
14. [Resources](#resources)
15. [Disclaimer](#disclaimer)

## Overview

Customer support teams often receive repetitive questions about orders, shipping, refunds, product features, account access, subscriptions, and policies. Responding to the same requests across websites, email, messaging apps, and phone calls can slow down service and fragment customer context.

**[ChatCactus](https://chatcactus.com/)** is an **[AI customer support platform](https://chatcactus.com/)** designed to help organizations create AI agents grounded in their own business documents and deploy those agents across customer communication channels. Its aim is to make common answers available quickly while preserving a path to a human teammate when a conversation needs personal attention.

The platform brings together knowledge management, AI responses, multi-channel communication, lead capture, escalation workflows, team administration, and developer integrations. Businesses can configure an agent once and use the same underlying knowledge across supported channels, with replies adapted to the communication format.

This GitHub repository is a **separate educational chatbot example**. It is intended for learning and experimentation, **not** as the source code for the commercial ChatCactus service.

## About the Educational Repository

**Repository:** https://github.com/rascal7866/ai-customer-support-chatbot

This project is an educational starting point for exploring automated customer support workflows and chatbot design. It can help developers understand how customer questions, response logic, test cases, and support-oriented examples fit together.

### Learning objectives

- Understand the structure of a customer-support chatbot project.
- Explore how frequently asked questions can be handled consistently.
- Practice organizing chatbot logic and examples into maintainable files.
- Learn why automated tests matter for customer-facing workflows.
- Consider future enhancements such as retrieval, escalation, analytics, and channel integrations.

### Important distinction

| Educational GitHub repository | Hosted ChatCactus platform |
| --- | --- |
| A learning-oriented code example | A commercial AI customer support service |
| Demonstrates concepts through its included code | Offers the platform capabilities described below |
| Features depend on what is actually implemented in this repository | Product features and availability are documented on the official website |
| Does not automatically include hosted integrations, billing, or dashboard functionality | Provides managed channels, administration, and integrations subject to plan and configuration |

**Do not assume that a platform feature listed below is implemented in this repository.** Review the source files and tests to determine the demo's actual scope.

## About the ChatCactus Platform

The hosted **[AI customer support platform](https://chatcactus.com/)** enables businesses to configure AI agents that use company-approved knowledge rather than relying solely on generic model knowledge. Teams can upload reference material, define an agent's role and tone, connect communication channels, and review conversations requiring intervention.

ChatCactus is relevant to businesses that want to reduce repetitive support work, offer timely answers outside standard business hours, maintain consistent responses, and capture potential customer inquiries without building an entire AI-support infrastructure from scratch.

### Key goals

- **Faster answers:** Provide prompt responses to common customer questions.
- **Knowledge consistency:** Ground replies in uploaded business documents.
- **Omnichannel support:** Use a shared agent across supported communication channels.
- **Human oversight:** Transfer uncertain or sensitive conversations to a person.
- **Lead generation:** Collect useful contact details when appropriate.
- **Developer flexibility:** Connect external systems through APIs and webhooks.
- **Operational control:** Manage teams, permissions, usage, and costs.

## Core Platform Capabilities

### 1. AI chatbots trained on business knowledge

Teams can create agents and upload documents such as PDFs, Word files, plain text, Markdown, and supported structured files. The platform processes documents for retrieval so the agent can respond using relevant source material.

Rather than answering only from general model knowledge, the agent can reference approved documents such as refund policies, pricing information, service descriptions, FAQs, product catalogs, onboarding material, or internal procedures. Responses can include source citations, helping teams check where an answer came from.

**Learn more:** [ChatCactus features](https://chatcactus.com/features)

### 2. Knowledge-grounded responses and citations

Grounding is particularly important when a business has precise rules about returns, subscriptions, delivery times, or service coverage. ChatCactus describes a workflow in which uploaded material is indexed and relevant information is retrieved for the conversation.

When an answer cannot be supported by available sources, the agent is designed to acknowledge that limitation instead of inventing an answer. Teams can also configure escalation for cases that need review.

### 3. Website chat widget

A website widget gives visitors a place to ask questions while browsing. Businesses can use it for pre-sales questions, support requests, policy explanations, and contact collection. The official platform also describes voice input for the website widget.

This is useful for companies that want a customer-facing support option without requiring visitors to leave the website.

### 4. Multi-channel AI support

The platform supports a shared agent across website chat, email, messaging services, collaboration tools, and voice channels. The underlying knowledge and persona remain consistent while the response format adapts to the channel.

For example, an email response can be more detailed, an SMS response more concise, and a messaging-app response more conversational.

**Explore:** [Supported integrations](https://chatcactus.com/integrations)

### 5. Human escalation and agent handoff

Not every customer question should be handled automatically. Customers may request a human, or the AI may lack reliable source material. ChatCactus provides a human escalation workflow so team members can take over a conversation.

The platform describes an escalations queue with assignment, priority, internal notes, and a history of handoff events. The AI stops replying on the escalated thread while a teammate handles the request, reducing the risk of overlapping responses.

### 6. Lead capture and qualification

ChatCactus supports configurable lead forms for collecting contact information such as names, email addresses, and phone numbers. Businesses can choose when to request these details, including during a pre-chat experience or when a conversation indicates purchase interest.

Potential applications include booking inquiries, sales consultations, product demonstrations, and contact requests. The platform also describes deduplication and exportable lead information.

### 7. Voice AI for web and phone

For customers who prefer speaking, ChatCactus documents voice interaction through the website widget and inbound phone support. Voice conversations can be transcribed for follow-up and review.

Voice features may be particularly useful for accessibility, hands-free support, and businesses that receive telephone inquiries.

### 8. Team collaboration and permissions

The platform supports owner, admin, and member roles. Teams can invite colleagues, manage access, assign escalated conversations, and keep internal notes about support cases.

Role-based permissions help separate billing and administration from everyday support operations.

### 9. Conversation context and returning visitors

Customer interactions are more useful when an agent can retain appropriate conversation context. ChatCactus describes conversation memory and returning-visitor recognition capabilities, with availability depending on product configuration and plan.

This can reduce repeated explanations while allowing teams to review customer interaction histories.

### 10. AI usage and cost controls

Businesses need visibility into how many AI messages they use and what those interactions cost. ChatCactus documents usage limits, per-message cost tracking, and workspace-level cost ceilings with model-routing controls.

These features can help teams budget for AI-powered support as usage grows.

## Supported Communication Channels

The official ChatCactus integrations page describes the following channels and connection methods:

| Channel | Example use |
| --- | --- |
| Website widget | Help visitors on product, pricing, and support pages |
| Gmail | Respond to customer inquiries in email threads |
| SMS via Twilio | Handle concise two-way text conversations |
| WhatsApp | Answer customer messages in a familiar messaging app |
| Telegram | Provide support through a Telegram bot |
| Slack | Assist teams through messages and mentions |
| Discord | Answer community questions |
| Facebook Messenger | Support conversations from a connected Facebook Page |
| Phone calls | Handle inbound spoken customer inquiries |
| Custom webhooks | Connect external workflows, automation services, or internal systems |

**Note:** Channel availability, setup requirements, and plan access can change. Consult the [official integrations page](https://chatcactus.com/integrations) before deploying.

## How the Platform Works

A typical ChatCactus deployment follows this process:

1. **Create a workspace and agent.** Configure the agent's purpose, tone, and basic behavior.
2. **Add knowledge sources.** Upload documents containing approved answers, policies, and product information.
3. **Review and test answers.** Ask representative customer questions and verify that replies are supported by the source material.
4. **Connect channels.** Add the website widget or configure supported messaging, email, or voice integrations.
5. **Configure lead capture and escalation.** Decide when the agent should collect details or transfer a conversation to a person.
6. **Publish and monitor.** Review conversations, refine documents, and adjust configuration as customer needs evolve.

The same knowledge foundation can serve multiple channels, reducing the need to maintain separate support content for each integration.

## Who Can Benefit

### Small businesses

Small businesses may not have a dedicated support team available at every hour. A knowledge-grounded AI assistant can help answer common questions about hours, services, prices, availability, and policies while providing a human contact path for complex issues.

### E-commerce stores

Online retailers receive frequent questions about shipping, returns, exchanges, payment options, and product details. A chatbot trained on store policies can help customers find relevant information and direct unresolved order-specific issues to staff.

### SaaS companies

Software businesses can use AI support to explain product features, onboarding steps, account policies, subscription plans, and troubleshooting guides. Documentation-grounded responses can reduce repeated introductory questions.

### Agencies and service businesses

Marketing agencies, consultancies, and professional service providers can use conversational forms to capture inquiries, explain service offerings, and direct qualified leads to a sales representative.

### Internal support teams

An internal help desk can use approved documentation to answer common HR, IT, operations, or onboarding questions, while escalating cases that require human judgment or privileged access.

## Common Business Use Cases

### Frequently asked questions

Use approved FAQ and policy documents to provide consistent answers to recurring questions.

### Order and shipping inquiries

Explain published shipping policies, delivery expectations, and return procedures. Access to an individual order's live status requires an appropriate connected business system; a document-only agent should not invent order details.

### Subscription and billing guidance

Explain available subscription plans, renewal rules, billing policies, and cancellation instructions from current source documents.

### Lead generation

Answer pre-sales questions and collect contact information for interested visitors, with appropriate privacy disclosures.

### Product onboarding

Help new users navigate documentation, feature explanations, and setup instructions.

### Escalation to a human agent

Route unsupported, urgent, or sensitive requests to staff for review and direct follow-up.

### Community and team assistance

Make approved information available through supported workplace and community channels.

## Security, Privacy, and Administration

The hosted platform documents several security and administrative practices:

- Encrypted integration credentials.
- Hashed passwords and API keys.
- Revocable API credentials and rate limiting.
- Domain restrictions for embedded agents.
- Workspace roles and team permissions.
- Usage quotas and spending controls.
- Human oversight and escalation workflows.

Businesses remain responsible for using the platform appropriately, obtaining required consents, reviewing AI responses, and managing the information they upload. Consult the official [privacy policy](https://chatcactus.com/privacy), [terms](https://chatcactus.com/terms), and [features page](https://chatcactus.com/features) for details.

## Developer API and Integrations

ChatCactus documents a public REST API for interacting with published agents from other applications. The API uses JSON requests and responses, bearer-key authentication, and supports streaming responses.

**Official API documentation:** https://chatcactus.com/docs

### Example: hosted ChatCactus API request

The following is an illustrative request for the **hosted platform**, not an endpoint supplied by this educational GitHub repository:

```bash
curl -X POST https://chatcactus.com/api/v1/chat \
  -H "Authorization: Bearer YOUR_CHATCACTUS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "agentId": "YOUR_PUBLISHED_AGENT_UUID",
    "message": "What is your refund policy?"
  }'
```

Create a valid API key and published agent through your ChatCactus account before using the example. Never commit real API keys to GitHub or expose secret keys in browser-side code.

The platform also documents custom webhooks that can support connections with automation tools and private systems. Review the official documentation for current endpoints, authentication requirements, limits, and supported integration behavior.

## Plans and Getting Started

ChatCactus advertises a free starting option for building and testing agents, alongside paid plans for broader deployment and team needs. Paid plan capabilities can differ by number of agents, messages, documents, team members, branding options, and other limits.

For current pricing, trials, and entitlements, always refer to the official [ChatCactus pricing page](https://chatcactus.com/pricing). Prices and plan features can change and are intentionally not hard-coded here.

To explore the hosted platform:

1. Visit [ChatCactus](https://chatcactus.com/).
2. Create an account or explore the available trial options.
3. Build an agent and upload sample knowledge documents.
4. Test common questions in the playground or widget.
5. Review integrations, security settings, and escalation workflows before publishing.

## Educational Project: Running and Testing

This repository is an independent learning project. Its exact entry points and dependencies should be checked in the source tree before running it.

### Clone the repository

```bash
git clone https://github.com/rascal7866/ai-customer-support-chatbot.git
cd ai-customer-support-chatbot
```

### Inspect the included files

Review the repository's source files, any dependency manifest, example data, and tests. Install only the dependencies actually declared by the project.

### Run the included tests

If the project contains Python `unittest` tests in a `tests/` directory, a common command is:

```bash
python -m unittest discover -s tests -v
```

This is a standard Python testing command, **not a guarantee** that every version of this repository uses that test structure. If the repository documents another test runner, follow its instructions instead.

### Suggested areas for future experimentation

- Retrieval-augmented answers using approved documents.
- Evaluation of response quality and source grounding.
- A human-handoff simulation for uncertain questions.
- Conversation logging with appropriate privacy controls.
- Unit tests for common support scenarios.
- A simple user interface or API layer.
- Safe handling of environment variables and credentials.

These are **ideas for extending the educational project**, not claims about already implemented functionality.

## Frequently Asked Questions

### What is ChatCactus?

[ChatCactus](https://chatcactus.com/) is an AI customer support platform for building knowledge-grounded AI agents and deploying them across supported communication channels.

### Is ChatCactus suitable for small businesses?

The platform offers use cases for small teams that want to answer routine customer questions, capture inquiries, and route complex conversations to staff. Suitability depends on support volume, channel needs, privacy requirements, and budget.

### Can ChatCactus answer questions using my own documents?

Yes. The hosted platform describes document upload, indexing, retrieval, and cited answers based on the knowledge supplied by a business.

### Can an AI conversation be transferred to a person?

Yes. The hosted platform includes human escalation workflows and an assignment queue for staff.

### Does ChatCactus support WhatsApp and email?

The official integrations documentation lists WhatsApp and Gmail alongside website chat, SMS, Telegram, Slack, Discord, Messenger, phone calls, and custom webhooks.

### Is there a developer API?

Yes. The hosted service provides [API documentation](https://chatcactus.com/docs) covering published-agent chat endpoints, authentication, and streaming.

### Is this repository the full ChatCactus source code?

**No.** This is a separate educational chatbot repository inspired by the customer-support domain. It should not be treated as the official hosted platform's application code.

### Does this repository include all the features described above?

No such claim is made. The sections about channels, voice, lead capture, security, and hosted APIs describe the **ChatCactus commercial platform**. The repository's actual capabilities are limited to its committed code and tests.

## Resources

- **Official website:** [ChatCactus — AI customer support platform](https://chatcactus.com/)
- **Product features:** [Knowledge base, escalation, voice, and more](https://chatcactus.com/features)
- **Channel integrations:** [Supported channels and connections](https://chatcactus.com/integrations)
- **Developer documentation:** [ChatCactus REST API](https://chatcactus.com/docs)
- **Pricing:** [Plans and current limits](https://chatcactus.com/pricing)
- **Privacy:** [Privacy policy](https://chatcactus.com/privacy)
- **Terms:** [Terms of service](https://chatcactus.com/terms)
- **Educational repository:** [AI customer support chatbot on GitHub](https://github.com/rascal7866/ai-customer-support-chatbot)

## Disclaimer

This README describes two distinct things: an **independent educational GitHub chatbot project** and the **hosted ChatCactus product** that inspired its subject matter. Platform descriptions are based on publicly available ChatCactus product documentation and may change. Nothing here implies that the educational repository implements the commercial platform's complete feature set or includes its proprietary source code.

---
**Explore the [ChatCactus AI customer support platform](https://chatcactus.com/) to learn more about knowledge-grounded customer support automation, multi-channel AI agents, and human escalation.**
