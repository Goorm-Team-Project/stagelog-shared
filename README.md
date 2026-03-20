# shared-contracts

## Purpose
This repository contains cross-service contracts and carefully scoped runtime helpers.

## Allowed Contents
- Event type constants
- Event payload schemas and versioned DTO definitions
- Internal API request/response DTO schemas
- Shared error code enums (minimal)
- Shared HTTP/internal API helper functions used by multiple services
- Small framework glue with no service-specific DB ownership

## Not Allowed
- Django ORM models
- Service-owned business logic
- DB access code tied to a service model
- Service-specific settings and deployment code

## Versioning
- Contract changes must be backward-compatible when possible.
- Breaking changes require version bump and staged rollout.
