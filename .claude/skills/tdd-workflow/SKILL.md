---
name: tdd-workflow
description: Test-Driven Development guide using Red-Green-Refactor. Use when the user says "TDD", "write tests first", "test-driven", "add tests", "unit test", or wants help writing tests before code.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - Task
  - Write
  - Edit
---

# TDD Workflow Skill

Guide through Test-Driven Development using the Red-Green-Refactor cycle, helping you write better code with comprehensive test coverage.

## Invocation

This skill activates when:
- User wants to write tests before implementation
- User mentions "TDD", "test-driven development"
- User asks to "add tests" or "write tests first"
- User wants help with unit testing patterns

Arguments: `$ARGUMENTS` (function/feature to implement, or existing code to test)

---

## The Red-Green-Refactor Cycle

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│    ┌─────────┐     ┌─────────┐     ┌──────────┐           │
│    │  RED    │────▶│ GREEN   │────▶│ REFACTOR │           │
│    │         │     │         │     │          │           │
│    │ Write a │     │ Make it │     │ Clean up │           │
│    │ failing │     │ pass    │     │ the code │           │
│    │ test    │     │ quickly │     │          │           │
│    └─────────┘     └─────────┘     └──────────┘           │
│         ▲                               │                  │
│         │                               │                  │
│         └───────────────────────────────┘                  │
│              (repeat for next requirement)                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Phase 1: RED - Write a Failing Test

### Goals
- Define the expected behavior before implementation
- Test should fail for the right reason
- Keep tests small and focused

### Process

1. **Identify the requirement** - What should the code do?
2. **Write the test** - Express the requirement as a test
3. **Run the test** - Verify it fails (for the right reason)

### Test Structure: AAA Pattern

```
Arrange → Act → Assert
```

**Example (JavaScript/TypeScript)**:
```typescript
describe('calculateDiscount', () => {
  it('should apply 10% discount for orders over $100', () => {
    // Arrange
    const orderTotal = 150;

    // Act
    const result = calculateDiscount(orderTotal);

    // Assert
    expect(result).toBe(135); // 150 - 15 (10%)
  });
});
```

**Example (Python)**:
```python
def test_calculate_discount_applies_10_percent_over_100():
    # Arrange
    order_total = 150

    # Act
    result = calculate_discount(order_total)

    # Assert
    assert result == 135  # 150 - 15 (10%)
```

### Test Naming Convention

Use descriptive names that explain:
- What is being tested
- Under what conditions
- What is the expected result

**Pattern**: `should_<expected>_when_<condition>`

Examples:
- `should_return_zero_when_input_is_empty`
- `should_throw_error_when_user_not_found`
- `should_apply_discount_when_order_exceeds_minimum`

---

## Phase 2: GREEN - Make It Pass

### Goals
- Write the simplest code that makes the test pass
- Don't over-engineer
- Don't write more code than needed

### Rules

1. **Write minimal code** - Just enough to pass the test
2. **It's okay to hardcode** - You can refactor later
3. **Don't add features** - Only what the test requires
4. **Speed over elegance** - Clean up in refactor phase

### Example Progression

**Test**:
```typescript
it('should return "fizz" for multiples of 3', () => {
  expect(fizzBuzz(3)).toBe('fizz');
});
```

**First GREEN (simple)**:
```typescript
function fizzBuzz(n: number): string {
  return 'fizz'; // Just make it pass!
}
```

**After more tests, GREEN (complete)**:
```typescript
function fizzBuzz(n: number): string {
  if (n % 15 === 0) return 'fizzbuzz';
  if (n % 3 === 0) return 'fizz';
  if (n % 5 === 0) return 'buzz';
  return n.toString();
}
```

---

## Phase 3: REFACTOR - Clean the Code

### Goals
- Improve code quality without changing behavior
- Remove duplication
- Improve readability

### What to Refactor

- **Duplication** - DRY up repeated code
- **Naming** - Make variables and functions clearer
- **Structure** - Extract functions, simplify conditionals
- **Performance** - Only if needed and measured

### Refactoring Rules

1. **All tests must still pass** after refactoring
2. **Don't add new functionality** during refactor
3. **Small steps** - One change at a time
4. **Run tests frequently** - After each change

### Common Refactorings

| Smell | Refactoring |
|-------|-------------|
| Long function | Extract Method |
| Duplicate code | Extract Method, Parameterize |
| Complex conditional | Extract Method, Replace with Polymorphism |
| Long parameter list | Introduce Parameter Object |
| Magic numbers | Extract Constant |

---

## Edge Cases Checklist

When writing tests, consider these edge cases:

### Input Boundaries
- [ ] Empty input (null, undefined, empty string, empty array)
- [ ] Single element
- [ ] Maximum size/value
- [ ] Minimum size/value
- [ ] Boundary values (0, -1, MAX_INT)

### String Edge Cases
- [ ] Empty string
- [ ] Whitespace only
- [ ] Very long strings
- [ ] Special characters
- [ ] Unicode characters
- [ ] Case sensitivity

### Number Edge Cases
- [ ] Zero
- [ ] Negative numbers
- [ ] Floating point precision
- [ ] Very large numbers
- [ ] Very small numbers
- [ ] NaN, Infinity

### Collection Edge Cases
- [ ] Empty collection
- [ ] Single item
- [ ] Duplicate items
- [ ] Sorted vs unsorted
- [ ] Null items in collection

### Error Conditions
- [ ] Invalid input types
- [ ] Missing required fields
- [ ] Network failures (for async)
- [ ] Timeouts
- [ ] Permission errors

---

## Mocking and Test Doubles

### When to Mock

Mock external dependencies:
- Database calls
- API requests
- File system
- Time/dates
- Random number generation

### Types of Test Doubles

| Type | Purpose | Example |
|------|---------|---------|
| **Stub** | Provides canned responses | Return fake user data |
| **Mock** | Verifies interactions | Check if email was sent |
| **Spy** | Records calls for later verification | Track function calls |
| **Fake** | Working implementation for testing | In-memory database |

### Mocking Example (JavaScript)

```typescript
// Using Jest
describe('UserService', () => {
  it('should send welcome email when user is created', async () => {
    // Arrange
    const mockEmailService = {
      sendWelcomeEmail: jest.fn().mockResolvedValue(true)
    };
    const userService = new UserService(mockEmailService);

    // Act
    await userService.createUser({ email: 'test@example.com' });

    // Assert
    expect(mockEmailService.sendWelcomeEmail).toHaveBeenCalledWith('test@example.com');
  });
});
```

### Mocking Example (Python)

```python
from unittest.mock import Mock, patch

def test_user_creation_sends_welcome_email():
    # Arrange
    mock_email_service = Mock()
    user_service = UserService(email_service=mock_email_service)

    # Act
    user_service.create_user(email='test@example.com')

    # Assert
    mock_email_service.send_welcome_email.assert_called_once_with('test@example.com')
```

---

## Test Organization

### File Structure

```
src/
  utils/
    calculator.ts
    calculator.test.ts    # Co-located tests
  services/
    user.service.ts
    user.service.test.ts

# OR

src/
  utils/
    calculator.ts
tests/
  utils/
    calculator.test.ts    # Mirrored structure
```

### Test Categories

```typescript
describe('Calculator', () => {
  describe('add', () => {
    it('should add two positive numbers', () => { /* ... */ });
    it('should handle negative numbers', () => { /* ... */ });
    it('should handle zero', () => { /* ... */ });
  });

  describe('divide', () => {
    it('should divide two numbers', () => { /* ... */ });
    it('should throw error when dividing by zero', () => { /* ... */ });
  });
});
```

---

## TDD Workflow Commands

### JavaScript/TypeScript (Jest)

```bash
# Run all tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run specific test file
npm test -- calculator.test.ts

# Run tests matching pattern
npm test -- -t "should add"

# Generate coverage report
npm test -- --coverage
```

### Python (pytest)

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_calculator.py

# Run tests matching pattern
pytest -k "test_add"

# Generate coverage report
pytest --cov=src
```

### Go

```bash
# Run all tests
go test ./...

# Run with verbose output
go test -v ./...

# Run specific package tests
go test ./pkg/calculator

# Generate coverage
go test -cover ./...
```

---

## Quick Reference: Writing Good Tests

### Test Independence
- Each test should be independent
- Don't rely on test execution order
- Reset state between tests

### Test Speed
- Unit tests should be fast (<100ms each)
- Mock slow dependencies
- Run fast tests frequently

### Test Reliability
- Tests should be deterministic
- Mock time, randomness, external services
- Avoid flaky tests

### Test Readability
- One assertion per test (generally)
- Clear test names
- Arrange-Act-Assert structure
- Use helper functions for setup

---

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Testing implementation details | Brittle tests | Test behavior, not implementation |
| Too many assertions | Hard to diagnose failures | One assertion per test |
| Shared state between tests | Flaky, order-dependent | Reset state in setup/teardown |
| Overly complex setup | Hard to understand | Extract to helper functions |
| Testing private methods | Coupling to implementation | Test through public interface |
| Ignoring failing tests | Technical debt | Fix or delete |
