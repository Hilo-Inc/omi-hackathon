# Language-Specific Code Review Checklists

## TypeScript / JavaScript

### Type Safety
- [ ] Avoid `any` type - use proper types or `unknown`
- [ ] Null/undefined handled with optional chaining (`?.`) or nullish coalescing (`??`)
- [ ] Generic types used appropriately
- [ ] Type guards for narrowing union types
- [ ] No type assertions (`as`) without validation

### Async/Await
- [ ] All promises properly awaited or handled
- [ ] No floating promises (unhandled async calls)
- [ ] Error handling with try/catch for async operations
- [ ] Promise.all for concurrent independent operations
- [ ] Proper cleanup in finally blocks

### React Specific
- [ ] Hooks follow rules (top level, not conditional)
- [ ] useEffect dependencies complete and correct
- [ ] useMemo/useCallback for expensive operations
- [ ] Keys on list items are stable and unique
- [ ] No state updates after unmount
- [ ] Props destructured with proper types

### Node.js
- [ ] Environment variables validated at startup
- [ ] File paths sanitized (no path traversal)
- [ ] Streams properly closed/destroyed
- [ ] Process signals handled (SIGTERM, SIGINT)
- [ ] No synchronous file operations in hot paths

---

## Python

### Code Quality
- [ ] Type hints on function signatures
- [ ] Docstrings on public functions/classes
- [ ] Context managers (`with`) for resources
- [ ] List/dict comprehensions where appropriate
- [ ] No mutable default arguments

### Error Handling
- [ ] Specific exception types caught (not bare `except:`)
- [ ] Exceptions re-raised with context (`raise from`)
- [ ] Custom exceptions for domain errors
- [ ] Logging includes exception info

### Performance
- [ ] Generators for large sequences
- [ ] Set/dict for membership testing (not lists)
- [ ] String building with `join()` not `+`
- [ ] Lazy imports for heavy modules

### Django/Flask
- [ ] ORM queries optimized (select_related, prefetch_related)
- [ ] No raw SQL without parameterization
- [ ] Views have proper permission checks
- [ ] Forms/serializers validate all input
- [ ] Migrations are reversible

---

## Go

### Error Handling
- [ ] All errors checked (no `_` for errors)
- [ ] Errors wrapped with context (`fmt.Errorf` with `%w`)
- [ ] Custom error types implement `Error()` interface
- [ ] Sentinel errors for expected conditions

### Concurrency
- [ ] Goroutines have proper lifecycle management
- [ ] Channels closed by sender only
- [ ] Context propagated for cancellation
- [ ] No data races (use `go run -race`)
- [ ] WaitGroups for goroutine synchronization

### Resource Management
- [ ] `defer` for cleanup operations
- [ ] HTTP response bodies closed
- [ ] Database connections returned to pool
- [ ] Files closed after use

### Style
- [ ] Exported names have doc comments
- [ ] Receiver names consistent per type
- [ ] Interface segregation (small interfaces)
- [ ] Package names lowercase, single word

---

## Rust

### Safety
- [ ] Minimal use of `unsafe` blocks
- [ ] Unsafe code properly documented
- [ ] No unwrap() in production paths
- [ ] ? operator for error propagation

### Ownership
- [ ] Cloning only when necessary
- [ ] References preferred over ownership transfer
- [ ] Lifetimes explicitly annotated where needed
- [ ] No unnecessary `Rc`/`Arc`

### Error Handling
- [ ] Custom error types with `thiserror` or similar
- [ ] Result types for fallible operations
- [ ] Error context added with `anyhow` or custom

### Performance
- [ ] Iterators used instead of manual loops
- [ ] `&str` preferred over `String` for parameters
- [ ] `Vec` pre-allocated when size known
- [ ] Zero-copy parsing where possible

---

## SQL

### Query Safety
- [ ] Parameterized queries (no string concatenation)
- [ ] Input validated before reaching SQL
- [ ] LIMIT on unbounded queries
- [ ] Proper escaping for identifiers

### Performance
- [ ] Indexes exist for WHERE/JOIN columns
- [ ] No SELECT * in production code
- [ ] Queries explain-analyzed for efficiency
- [ ] Batch operations for bulk inserts/updates
- [ ] Connection pooling configured

### Schema Design
- [ ] Foreign keys with proper ON DELETE behavior
- [ ] NOT NULL constraints where appropriate
- [ ] Default values documented
- [ ] Migrations reversible

---

## Flutter / Dart

### Widget Design
- [ ] StatelessWidget when no internal state needed
- [ ] const constructors where possible
- [ ] Keys provided for dynamic lists
- [ ] Build methods are pure (no side effects)
- [ ] Widgets extracted for reusability

### State Management
- [ ] State properly disposed (controllers, streams)
- [ ] Riverpod providers scoped appropriately
- [ ] No business logic in widgets
- [ ] Loading/error states handled

### Performance
- [ ] Images cached and sized appropriately
- [ ] Lists use ListView.builder for large datasets
- [ ] Expensive computations in compute() isolate
- [ ] Rebuilds minimized with selective providers

### Null Safety
- [ ] Late variables properly initialized
- [ ] Null checks before dereferencing
- [ ] Required parameters marked `required`
- [ ] Default values for optional parameters

---

## General API Design

### REST APIs
- [ ] Proper HTTP methods (GET read, POST create, etc.)
- [ ] Meaningful status codes (201 created, 404 not found)
- [ ] Consistent error response format
- [ ] Pagination for list endpoints
- [ ] Rate limiting considered

### Request Handling
- [ ] Input validation on all endpoints
- [ ] Request size limits configured
- [ ] Timeout handling
- [ ] Idempotency for write operations

### Response Design
- [ ] Consistent response envelope
- [ ] No sensitive data in responses
- [ ] Proper content-type headers
- [ ] CORS configured appropriately
