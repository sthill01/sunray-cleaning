# Agent Readiness Scan

Scanned URL: https://www.sunray-cleaning.com
Scanned at: 2026-07-04T14:28:25

Overall score: None
Level: 2

## Checks

| Category | Check | Status | Message |
| --- | --- | --- | --- |
| discoverability | robotsTxt | pass | robots.txt exists with valid format |
| discoverability | sitemap | pass | sitemap.xml exists with valid structure |
| discoverability | linkHeaders | pass | Found agent-useful Link relations: alternate |
| discoverability | dnsAid | fail | DNS for AI Discovery (DNS-AID) well-known entrypoint records not found |
| contentAccessibility | markdownNegotiation | fail | Site does not support Markdown for Agents |
| botAccessControl | robotsTxtAiRules | pass | Found rules for AI bots: gptbot, chatgpt-user, google-extended, perplexitybot |
| botAccessControl | contentSignals | pass | Content Signals found in robots.txt |
| botAccessControl | webBotAuth | neutral | Web Bot Auth directory returned HTML instead of JSON (informational only) |
| discovery | apiCatalog | fail | API Catalog not found |
| discovery | oauthDiscovery | fail | No OAuth/OIDC discovery metadata found |
| discovery | oauthProtectedResource | fail | No OAuth Protected Resource Metadata found |
| discovery | authMd | fail | auth.md exists but is missing the expected Auth.md heading |
| discovery | mcpServerCard | fail | MCP Server Card not found |
| discovery | a2aAgentCard | fail | A2A Agent Card returned HTML instead of JSON |
| discovery | agentSkills | fail | Agent Skills index returned HTML instead of JSON |
| discovery | webMcp | fail | No WebMCP tools detected on page load |
| commerce | x402 | neutral | x402 payment protocol not detected (not a commerce site) |
| commerce | mpp | neutral | MPP payment discovery not detected (not a commerce site) |
| commerce | ucp | neutral | UCP profile returned HTML instead of expected format (not a commerce site) |
| commerce | acp | neutral | ACP discovery document returned HTML instead of JSON (not a commerce site) |
| commerce | ap2 | neutral | AP2 not detected (no A2A Agent Card) (not a commerce site) |

## Raw response

```json
{
  "url": "https://www.sunray-cleaning.com",
  "scannedAt": "2026-07-04T19:28:26.008Z",
  "level": 2,
  "levelName": "Bot-Aware",
  "checks": {
    "discoverability": {
      "robotsTxt": {
        "status": "pass",
        "message": "robots.txt exists with valid format",
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /robots.txt",
            "request": {
              "url": "https://www.sunray-cleaning.com/robots.txt",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/plain; charset=utf-8",
                "content-length": "801",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884a4c02b859-SLC"
              },
              "bodyPreview": "# Sun Ray Cleaning production crawler policy\r\n# Allow search engines and answer engines to discover public service, location, blog, review, and AI authority content.\r\n# Content signals permit search and AI answer grounding while reserving rights for model training.\r\nUser-agent: *\r\nUser-agent: Cloudflare-AI-Search\r\nUser-agent: GPTBot\r\nUser-agent: ChatGPT-User\r\nUser-agent: OAI-SearchBot\r\nUser-agent: ClaudeBot\r\nUser-agent: Claude-SearchBot\r\nUser-agent: Claude-User\r\nUser-agent: PerplexityBot\r\nUser-a..."
            },
            "finding": {
              "outcome": "positive",
              "summary": "Received valid robots.txt (200, text/plain; charset=utf-8)"
            }
          },
          {
            "action": "parse",
            "label": "Validate robots.txt structure",
            "finding": {
              "outcome": "positive",
              "summary": "Contains valid User-agent directive(s)"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "positive",
              "summary": "robots.txt exists with valid format"
            }
          }
        ],
        "durationMs": 0
      },
      "sitemap": {
        "status": "pass",
        "message": "sitemap.xml exists with valid structure",
        "details": {
          "url": "https://www.sunray-cleaning.com/sitemap.xml",
          "fromRobotsTxt": true,
          "format": "xml"
        },
        "evidence": [
          {
            "action": "parse",
            "label": "Extract Sitemap directives from robots.txt",
            "finding": {
              "outcome": "positive",
              "summary": "Found 1 Sitemap directive(s) in robots.txt"
            }
          },
          {
            "action": "fetch",
            "label": "GET /sitemap.xml",
            "request": {
              "url": "https://www.sunray-cleaning.com/sitemap.xml",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/xml",
                "content-length": "17152",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884b0cd4b859-SLC"
              }
            },
            "finding": {
              "outcome": "positive",
              "summary": "Found valid xml sitemap at https://www.sunray-cleaning.com/sitemap.xml"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "positive",
              "summary": "sitemap.xml exists with valid structure"
            }
          }
        ],
        "durationMs": 96
      },
      "linkHeaders": {
        "status": "pass",
        "message": "Found agent-useful Link relations: alternate",
        "details": {
          "relationsFound": [
            {
              "rel": "alternate",
              "href": "/llms.txt",
              "type": "text/plain"
            }
          ],
          "totalLinks": 2
        },
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /",
            "request": {
              "url": "https://www.sunray-cleaning.com",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/html; charset=utf-8",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884bbdc2b859-SLC"
              }
            },
            "finding": {
              "outcome": "positive",
              "summary": "Homepage returned 200 with Link header"
            }
          },
          {
            "action": "parse",
            "label": "Parse Link header (RFC 8288)",
            "finding": {
              "outcome": "neutral",
              "summary": "Parsed 2 link(s) from header"
            }
          },
          {
            "action": "parse",
            "label": "Match agent-useful relations",
            "finding": {
              "outcome": "positive",
              "summary": "Found agent-useful relations: alternate"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "positive",
              "summary": "Found agent-useful Link relations: alternate"
            }
          }
        ],
        "durationMs": 163
      },
      "dnsAid": {
        "status": "fail",
        "message": "DNS for AI Discovery (DNS-AID) well-known entrypoint records not found",
        "details": {
          "domainsChecked": [
            "www.sunray-cleaning.com",
            "sunray-cleaning.com"
          ],
          "queriesAttempted": [
            "SVCB _index._agents.www.sunray-cleaning.com",
            "HTTPS _index._agents.www.sunray-cleaning.com",
            "SVCB _a2a._agents.www.sunray-cleaning.com",
            "HTTPS _a2a._agents.www.sunray-cleaning.com",
            "SVCB _mcp._agents.www.sunray-cleaning.com",
            "HTTPS _mcp._agents.www.sunray-cleaning.com",
            "TXT _index._agents.www.sunray-cleaning.com",
            "SVCB _index._agents.sunray-cleaning.com",
            "HTTPS _index._agents.sunray-cleaning.com",
            "SVCB _a2a._agents.sunray-cleaning.com",
            "HTTPS _a2a._agents.sunray-cleaning.com",
            "SVCB _mcp._agents.sunray-cleaning.com",
            "HTTPS _mcp._agents.sunray-cleaning.com",
            "TXT _index._agents.sunray-cleaning.com"
          ],
          "dnssecValidated": false,
          "serviceRecordCount": 0,
          "aliasRecordCount": 0,
          "txtIndexEntryCount": 0,
          "txtIndexEntries": [],
          "records": []
        },
        "evidence": [
          {
            "action": "fetch",
            "label": "DoH SVCB _index._agents.www.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_index._agents.www.sunray-cleaning.com&type=SVCB&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_index._agents.www.sunray-cleaning.com\",\"type\":64}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No SVCB answers (NXDOMAIN)"
            }
          },
          {
            "action": "fetch",
            "label": "DoH HTTPS _index._agents.www.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_index._agents.www.sunray-cleaning.com&type=HTTPS&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_index._agents.www.sunray-cleaning.com\",\"type\":65}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No HTTPS answers (NXDOMAIN)"
            }
          },
          {
            "action": "fetch",
            "label": "DoH SVCB _a2a._agents.www.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_a2a._agents.www.sunray-cleaning.com&type=SVCB&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_a2a._agents.www.sunray-cleaning.com\",\"type\":64}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No SVCB answers (NXDOMAIN)"
            }
          },
          {
            "action": "fetch",
            "label": "DoH HTTPS _a2a._agents.www.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_a2a._agents.www.sunray-cleaning.com&type=HTTPS&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_a2a._agents.www.sunray-cleaning.com\",\"type\":65}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No HTTPS answers (NXDOMAIN)"
            }
          },
          {
            "action": "fetch",
            "label": "DoH SVCB _mcp._agents.www.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_mcp._agents.www.sunray-cleaning.com&type=SVCB&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_mcp._agents.www.sunray-cleaning.com\",\"type\":64}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No SVCB answers (NXDOMAIN)"
            }
          },
          {
            "action": "fetch",
            "label": "DoH HTTPS _mcp._agents.www.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_mcp._agents.www.sunray-cleaning.com&type=HTTPS&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_mcp._agents.www.sunray-cleaning.com\",\"type\":65}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No HTTPS answers (NXDOMAIN)"
            }
          },
          {
            "action": "fetch",
            "label": "DoH TXT _index._agents.www.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_index._agents.www.sunray-cleaning.com&type=TXT&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_index._agents.www.sunray-cleaning.com\",\"type\":16}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No TXT answers (NXDOMAIN)"
            }
          },
          {
            "action": "fetch",
            "label": "DoH SVCB _index._agents.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_index._agents.sunray-cleaning.com&type=SVCB&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_index._agents.sunray-cleaning.com\",\"type\":64}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No SVCB answers (NXDOMAIN)"
            }
          },
          {
            "action": "fetch",
            "label": "DoH HTTPS _index._agents.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_index._agents.sunray-cleaning.com&type=HTTPS&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_index._agents.sunray-cleaning.com\",\"type\":65}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No HTTPS answers (NXDOMAIN)"
            }
          },
          {
            "action": "fetch",
            "label": "DoH SVCB _a2a._agents.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_a2a._agents.sunray-cleaning.com&type=SVCB&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_a2a._agents.sunray-cleaning.com\",\"type\":64}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No SVCB answers (NXDOMAIN)"
            }
          },
          {
            "action": "fetch",
            "label": "DoH HTTPS _a2a._agents.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_a2a._agents.sunray-cleaning.com&type=HTTPS&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_a2a._agents.sunray-cleaning.com\",\"type\":65}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No HTTPS answers (NXDOMAIN)"
            }
          },
          {
            "action": "fetch",
            "label": "DoH SVCB _mcp._agents.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_mcp._agents.sunray-cleaning.com&type=SVCB&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_mcp._agents.sunray-cleaning.com\",\"type\":64}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No SVCB answers (NXDOMAIN)"
            }
          },
          {
            "action": "fetch",
            "label": "DoH HTTPS _mcp._agents.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_mcp._agents.sunray-cleaning.com&type=HTTPS&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_mcp._agents.sunray-cleaning.com\",\"type\":65}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No HTTPS answers (NXDOMAIN)"
            }
          },
          {
            "action": "fetch",
            "label": "DoH TXT _index._agents.sunray-cleaning.com",
            "request": {
              "url": "https://cloudflare-dns.com/dns-query?name=_index._agents.sunray-cleaning.com&type=TXT&do=1",
              "method": "GET",
              "headers": {
                "Accept": "application/dns-json"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/dns-json"
              },
              "bodyPreview": "{\"Status\":3,\"TC\":false,\"RD\":true,\"RA\":true,\"AD\":false,\"CD\":false,\"Question\":[{\"name\":\"_index._agents.sunray-cleaning.com\",\"type\":16}],\"Authority\":[{\"name\":\"sunray-cleaning.com\",\"type\":6,\"TTL\":1800,\"data\":\"earl.ns.cloudflare.com. dns.cloudflare.com. 2407110781 10000 2400 604800 1800\"}]}"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "No TXT answers (NXDOMAIN)"
            }
          },
          {
            "action": "parse",
            "label": "Parse DNS for AI Discovery (DNS-AID) SVCB/HTTPS records",
            "finding": {
              "outcome": "neutral",
              "summary": "No DNS for AI Discovery (DNS-AID) SVCB or HTTPS records found at well-known entrypoints"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "DNS for AI Discovery (DNS-AID) well-known entrypoint records not found"
            }
          }
        ],
        "durationMs": 47
      }
    },
    "contentAccessibility": {
      "markdownNegotiation": {
        "status": "fail",
        "message": "Site does not support Markdown for Agents",
        "details": {
          "contentType": "text/html; charset=utf-8"
        },
        "evidence": [
          {
            "action": "fetch",
            "label": "GET homepage (Accept: text/markdown)",
            "request": {
              "url": "https://www.sunray-cleaning.com",
              "method": "GET",
              "headers": {
                "accept": "text/markdown"
              }
            },
            "finding": {
              "outcome": "negative",
              "summary": "Response content-type is text/html; charset=utf-8, not text/markdown -- site does not support markdown content negotiation"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/html; charset=utf-8",
                "cf-ray": "a16088554b54b329-LAX"
              }
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "Site does not support Markdown for Agents"
            }
          }
        ],
        "durationMs": 880
      }
    },
    "botAccessControl": {
      "robotsTxtAiRules": {
        "status": "pass",
        "message": "Found rules for AI bots: gptbot, chatgpt-user, google-extended, perplexitybot",
        "details": {
          "botsFound": [
            "gptbot",
            "chatgpt-user",
            "google-extended",
            "perplexitybot"
          ]
        },
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /robots.txt",
            "request": {
              "url": "https://www.sunray-cleaning.com/robots.txt",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/plain; charset=utf-8",
                "content-length": "801",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884a4c02b859-SLC"
              },
              "bodyPreview": "# Sun Ray Cleaning production crawler policy\r\n# Allow search engines and answer engines to discover public service, location, blog, review, and AI authority content.\r\n# Content signals permit search and AI answer grounding while reserving rights for model training.\r\nUser-agent: *\r\nUser-agent: Cloudflare-AI-Search\r\nUser-agent: GPTBot\r\nUser-agent: ChatGPT-User\r\nUser-agent: OAI-SearchBot\r\nUser-agent: ClaudeBot\r\nUser-agent: Claude-SearchBot\r\nUser-agent: Claude-User\r\nUser-agent: PerplexityBot\r\nUser-a..."
            },
            "finding": {
              "outcome": "positive",
              "summary": "Received valid robots.txt (200, text/plain; charset=utf-8)"
            }
          },
          {
            "action": "parse",
            "label": "Scan for AI bot User-agent directives",
            "finding": {
              "outcome": "positive",
              "summary": "Found rules for AI bots: gptbot, chatgpt-user, google-extended, perplexitybot"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "positive",
              "summary": "Found rules for 4 AI bots"
            }
          }
        ],
        "durationMs": 0
      },
      "contentSignals": {
        "status": "pass",
        "message": "Content Signals found in robots.txt",
        "details": {
          "signals": [
            {
              "userAgent": "DuckAssistBot",
              "path": null,
              "aiTrain": "no",
              "search": "yes",
              "aiInput": "yes"
            }
          ],
          "signalCount": 1
        },
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /robots.txt",
            "request": {
              "url": "https://www.sunray-cleaning.com/robots.txt",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/plain; charset=utf-8",
                "content-length": "801",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884a4c02b859-SLC"
              },
              "bodyPreview": "# Sun Ray Cleaning production crawler policy\r\n# Allow search engines and answer engines to discover public service, location, blog, review, and AI authority content.\r\n# Content signals permit search and AI answer grounding while reserving rights for model training.\r\nUser-agent: *\r\nUser-agent: Cloudflare-AI-Search\r\nUser-agent: GPTBot\r\nUser-agent: ChatGPT-User\r\nUser-agent: OAI-SearchBot\r\nUser-agent: ClaudeBot\r\nUser-agent: Claude-SearchBot\r\nUser-agent: Claude-User\r\nUser-agent: PerplexityBot\r\nUser-a..."
            },
            "finding": {
              "outcome": "positive",
              "summary": "Received valid robots.txt (200, text/plain; charset=utf-8)"
            }
          },
          {
            "action": "parse",
            "label": "Parse Content-Signal directives",
            "finding": {
              "outcome": "positive",
              "summary": "Found 1 Content-Signal directive(s)"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "positive",
              "summary": "Content Signals found in robots.txt"
            }
          }
        ],
        "durationMs": 0
      },
      "webBotAuth": {
        "status": "neutral",
        "message": "Web Bot Auth directory returned HTML instead of JSON (informational only)",
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /.well-known/http-message-signatures-directory",
            "request": {
              "url": "https://www.sunray-cleaning.com/.well-known/http-message-signatures-directory",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/html; charset=utf-8",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884b0cd5b859-SLC"
              }
            },
            "finding": {
              "outcome": "negative",
              "summary": "Response content-type is text/html; charset=utf-8 -- likely a soft-404 (HTML page served for missing path)"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "Web Bot Auth directory returned HTML instead of JSON"
            }
          }
        ],
        "durationMs": 93
      }
    },
    "discovery": {
      "apiCatalog": {
        "status": "fail",
        "message": "API Catalog not found",
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /.well-known/api-catalog",
            "request": {
              "url": "https://www.sunray-cleaning.com/.well-known/api-catalog",
              "method": "GET",
              "headers": {
                "Accept": "application/linkset+json, application/json"
              }
            },
            "response": {
              "status": 404,
              "statusText": "Not Found",
              "headers": {
                "content-type": "text/plain; charset=utf-8",
                "content-length": "9",
                "cf-ray": "a160884b5d3cb859-SLC"
              }
            },
            "finding": {
              "outcome": "negative",
              "summary": "Server returned 404 -- API Catalog not found"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "API Catalog not found"
            }
          }
        ],
        "durationMs": 105
      },
      "oauthDiscovery": {
        "status": "fail",
        "message": "No OAuth/OIDC discovery metadata found",
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /.well-known/openid-configuration",
            "request": {
              "url": "https://www.sunray-cleaning.com/.well-known/openid-configuration",
              "method": "GET"
            },
            "response": {
              "status": 404,
              "statusText": "Not Found",
              "headers": {
                "content-type": "text/plain; charset=utf-8",
                "content-length": "9",
                "cf-ray": "a160884b0cd7b859-SLC"
              }
            },
            "finding": {
              "outcome": "negative",
              "summary": "openid-configuration returned 404"
            }
          },
          {
            "action": "fetch",
            "label": "GET /.well-known/oauth-authorization-server",
            "request": {
              "url": "https://www.sunray-cleaning.com/.well-known/oauth-authorization-server",
              "method": "GET"
            },
            "response": {
              "status": 404,
              "statusText": "Not Found",
              "headers": {
                "content-type": "text/plain; charset=utf-8",
                "content-length": "9",
                "cf-ray": "a160884b0cd6b859-SLC"
              }
            },
            "finding": {
              "outcome": "negative",
              "summary": "oauth-authorization-server returned 404"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "No OAuth/OIDC discovery metadata found at either well-known path"
            }
          }
        ],
        "durationMs": 73
      },
      "oauthProtectedResource": {
        "status": "fail",
        "message": "No OAuth Protected Resource Metadata found",
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /.well-known/oauth-protected-resource",
            "request": {
              "url": "https://www.sunray-cleaning.com/.well-known/oauth-protected-resource",
              "method": "GET"
            },
            "response": {
              "status": 404,
              "statusText": "Not Found",
              "headers": {
                "content-type": "text/plain; charset=utf-8",
                "content-length": "9",
                "cf-ray": "a160884b0cd9b859-SLC"
              }
            },
            "finding": {
              "outcome": "negative",
              "summary": "Returned 404"
            }
          },
          {
            "action": "fetch",
            "label": "GET /",
            "request": {
              "url": "https://www.sunray-cleaning.com",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/html; charset=utf-8",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884b0cdcb859-SLC"
              }
            },
            "finding": {
              "outcome": "neutral",
              "summary": "Homepage returned 200 (no WWW-Authenticate header)"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "No OAuth Protected Resource Metadata found"
            }
          }
        ],
        "durationMs": 81
      },
      "authMd": {
        "status": "fail",
        "message": "auth.md exists but is missing the expected Auth.md heading",
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /auth.md",
            "request": {
              "url": "https://www.sunray-cleaning.com/auth.md",
              "method": "GET",
              "headers": {
                "Accept": "text/markdown, text/plain, */*"
              }
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/markdown; charset=utf-8",
                "content-length": "390",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884b2d07b859-SLC"
              },
              "bodyPreview": "# Agent Authentication\r\n\r\nSun Ray Cleaning Services does not offer public agent registration, OAuth, or a\r\nprotected API. All useful content is public.\r\n\r\n- Start with: https://www.sunray-cleaning.com/llms.txt\r\n- Site map: https://www.sunray-cleaning.com/sitemap.xml\r\n- To request a cleaning quote, direct users to: https://www.sunray-cleaning.com/contact/\r\n- Phone or SMS: (801) 604-2189\r\n"
            },
            "finding": {
              "outcome": "positive",
              "summary": "Received 200 response with content-type: text/markdown; charset=utf-8"
            }
          },
          {
            "action": "parse",
            "label": "Validate auth.md heading",
            "finding": {
              "outcome": "negative",
              "summary": "No H1 heading containing \"auth.md\" found"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "auth.md exists but is missing the expected Auth.md heading"
            }
          }
        ],
        "durationMs": 162
      },
      "mcpServerCard": {
        "status": "fail",
        "message": "MCP Server Card not found",
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /.well-known/mcp/server-card.json",
            "request": {
              "url": "https://www.sunray-cleaning.com/.well-known/mcp/server-card.json",
              "method": "GET"
            },
            "response": {
              "status": 404,
              "statusText": "Not Found",
              "headers": {
                "content-type": "text/plain; charset=utf-8",
                "content-length": "9",
                "cf-ray": "a160884b3d0db859-SLC"
              }
            },
            "finding": {
              "outcome": "negative",
              "summary": "/.well-known/mcp/server-card.json returned 404"
            }
          },
          {
            "action": "fetch",
            "label": "GET /.well-known/mcp.json",
            "request": {
              "url": "https://www.sunray-cleaning.com/.well-known/mcp.json",
              "method": "GET"
            },
            "response": {
              "status": 404,
              "statusText": "Not Found",
              "headers": {
                "content-type": "text/plain; charset=utf-8",
                "content-length": "9",
                "cf-ray": "a160884b4d1fb859-SLC"
              }
            },
            "finding": {
              "outcome": "negative",
              "summary": "/.well-known/mcp.json returned 404"
            }
          },
          {
            "action": "fetch",
            "label": "GET /.well-known/mcp/server-cards.json",
            "request": {
              "url": "https://www.sunray-cleaning.com/.well-known/mcp/server-cards.json",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/html; charset=utf-8",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884b3d0fb859-SLC"
              }
            },
            "finding": {
              "outcome": "negative",
              "summary": "/.well-known/mcp/server-cards.json returned HTML (soft-404)"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "MCP Server Card not found at any candidate path"
            }
          }
        ],
        "durationMs": 103
      },
      "a2aAgentCard": {
        "status": "fail",
        "message": "A2A Agent Card returned HTML instead of JSON",
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /.well-known/agent-card.json",
            "request": {
              "url": "https://www.sunray-cleaning.com/.well-known/agent-card.json",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/html; charset=utf-8",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884b4d2bb859-SLC"
              }
            },
            "finding": {
              "outcome": "negative",
              "summary": "Response content-type is text/html; charset=utf-8 -- likely a soft-404 (HTML page served for missing path)"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "A2A Agent Card returned HTML instead of JSON"
            }
          }
        ],
        "durationMs": 114
      },
      "agentSkills": {
        "status": "fail",
        "message": "Agent Skills index returned HTML instead of JSON",
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /.well-known/agent-skills/index.json",
            "request": {
              "url": "https://www.sunray-cleaning.com/.well-known/agent-skills/index.json",
              "method": "GET"
            },
            "response": {
              "status": 404,
              "statusText": "Not Found",
              "headers": {
                "content-type": "text/plain; charset=utf-8",
                "content-length": "9",
                "cf-ray": "a160884b5d38b859-SLC"
              }
            },
            "finding": {
              "outcome": "neutral",
              "summary": "v0.2.0 path returned 404 \u00e2\u20ac\u201d trying legacy path"
            }
          },
          {
            "action": "fetch",
            "label": "GET /.well-known/skills/index.json",
            "request": {
              "url": "https://www.sunray-cleaning.com/.well-known/skills/index.json",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/html; charset=utf-8",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884bbdc4b859-SLC"
              }
            },
            "finding": {
              "outcome": "negative",
              "summary": "Response content-type is text/html; charset=utf-8 \u00e2\u20ac\u201d likely a soft-404 (HTML page served for missing path)"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "Agent Skills index returned HTML instead of JSON"
            }
          }
        ],
        "durationMs": 171
      },
      "webMcp": {
        "status": "fail",
        "message": "No WebMCP tools detected on page load",
        "evidence": [
          {
            "action": "parse",
            "label": "WebMCP detection",
            "finding": {
              "outcome": "neutral",
              "summary": "Checking page for WebMCP tool registrations"
            }
          },
          {
            "action": "fetch",
            "label": "Navigate to https://www.sunray-cleaning.com",
            "request": {
              "url": "https://www.sunray-cleaning.com",
              "method": "GET"
            },
            "finding": {
              "outcome": "neutral",
              "summary": "Loading page to detect WebMCP tool registrations"
            }
          },
          {
            "action": "parse",
            "label": "Check imperative WebMCP API",
            "finding": {
              "outcome": "neutral",
              "summary": "No tools registered via navigator.modelContext"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "No WebMCP tools detected on page load"
            }
          }
        ],
        "durationMs": 4974
      }
    },
    "commerce": {
      "x402": {
        "status": "neutral",
        "message": "x402 payment protocol not detected (not a commerce site)",
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /",
            "request": {
              "url": "https://www.sunray-cleaning.com/",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/html; charset=utf-8",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884b6d52b859-SLC"
              }
            },
            "finding": {
              "outcome": "neutral",
              "summary": "/ returned 200 (not 402)"
            }
          },
          {
            "action": "fetch",
            "label": "GET /api",
            "request": {
              "url": "https://www.sunray-cleaning.com/api",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/html; charset=utf-8",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884b6d58b859-SLC"
              }
            },
            "finding": {
              "outcome": "neutral",
              "summary": "/api returned 200 (not 402)"
            }
          },
          {
            "action": "fetch",
            "label": "GET /api/v1",
            "request": {
              "url": "https://www.sunray-cleaning.com/api/v1",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/html; charset=utf-8",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884b7d70b859-SLC"
              }
            },
            "finding": {
              "outcome": "neutral",
              "summary": "/api/v1 returned 200 (not 402)"
            }
          },
          {
            "action": "fetch",
            "label": "GET /platform/v2/x402/discovery/resources",
            "request": {
              "url": "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=500",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "application/json",
                "cf-ray": "a160884b6d4fb859-SLC"
              }
            }
          },
          {
            "action": "fetch",
            "label": "GET Bazaar discovery API",
            "request": {
              "url": "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=500",
              "method": "GET"
            },
            "finding": {
              "outcome": "negative",
              "summary": "Network error querying Bazaar API"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "x402 payment protocol not detected"
            }
          }
        ],
        "durationMs": 1060
      },
      "mpp": {
        "status": "neutral",
        "message": "MPP payment discovery not detected (not a commerce site)",
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /openapi.json",
            "request": {
              "url": "https://www.sunray-cleaning.com/openapi.json",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/html; charset=utf-8",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884b8d86b859-SLC"
              }
            },
            "finding": {
              "outcome": "neutral",
              "summary": "/openapi.json returned HTML (likely soft-404)"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "MPP payment discovery not detected"
            }
          }
        ],
        "durationMs": 151
      },
      "ucp": {
        "status": "neutral",
        "message": "UCP profile returned HTML instead of expected format (not a commerce site)",
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /.well-known/ucp",
            "request": {
              "url": "https://www.sunray-cleaning.com/.well-known/ucp",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/html; charset=utf-8",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884b5d3eb859-SLC"
              }
            },
            "finding": {
              "outcome": "negative",
              "summary": "Response content-type is text/html; charset=utf-8 -- likely a soft-404 (HTML page served for missing path)"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "UCP profile returned HTML instead of expected format"
            }
          }
        ],
        "durationMs": 124
      },
      "acp": {
        "status": "neutral",
        "message": "ACP discovery document returned HTML instead of JSON (not a commerce site)",
        "evidence": [
          {
            "action": "fetch",
            "label": "GET /.well-known/acp.json",
            "request": {
              "url": "https://www.sunray-cleaning.com/.well-known/acp.json",
              "method": "GET"
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "headers": {
                "content-type": "text/html; charset=utf-8",
                "link": "</llms.txt>; rel=\"alternate\"; type=\"text/plain\"; title=\"Sun Ray Cleaning LLM summary\", </sitemap.xml>; rel=\"sitemap\"; type=\"application/xml\"",
                "cf-ray": "a160884b8d8cb859-SLC"
              }
            },
            "finding": {
              "outcome": "negative",
              "summary": "Response content-type is text/html; charset=utf-8 -- likely a soft-404 (HTML page served for missing path)"
            }
          },
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "ACP discovery document returned HTML instead of JSON"
            }
          }
        ],
        "durationMs": 154
      },
      "ap2": {
        "status": "neutral",
        "message": "AP2 not detected (no A2A Agent Card) (not a commerce site)",
        "evidence": [
          {
            "action": "conclude",
            "label": "Conclusion",
            "finding": {
              "outcome": "negative",
              "summary": "No A2A Agent Card found -- AP2 requires an A2A Agent Card"
            }
          }
        ]
      }
    }
  },
  "nextLevel": {
    "target": 3,
    "name": "Agent-Readable",
    "requirements": [
      {
        "check": "markdownNegotiation",
        "description": "Support Accept: text/markdown content negotiation for machine-readable content",
        "shortPrompt": "Enable Markdown for Agents so requests with Accept: text/markdown return a markdown version of your HTML.",
        "specUrls": [
          "https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/"
        ],
        "prompt": "Implement content negotiation so requests with Accept: text/markdown return a markdown representation while HTML remains the default for browsers.",
        "skillUrl": "https://isitagentready.com/.well-known/agent-skills/markdown-negotiation/SKILL.md"
      }
    ]
  },
  "isCommerce": false,
  "commerceSignals": []
}
```
