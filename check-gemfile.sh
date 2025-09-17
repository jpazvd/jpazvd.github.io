#!/bin/bash
# Gemfile Protection Script
# Run this before committing to ensure Gemfile integrity

echo "🔍 Checking Gemfile integrity..."

# Check for corruption patterns
if grep -q "source.*source" Gemfile; then
    echo "❌ CORRUPTION DETECTED: Duplicate source lines"
    echo "🔧 Restoring from backup..."
    cp Gemfile.backup Gemfile
    echo "✅ Gemfile restored"
elif grep -q "https://.*github.io" Gemfile; then
    echo "❌ CORRUPTION DETECTED: URL contamination"
    echo "🔧 Restoring from backup..."
    cp Gemfile.backup Gemfile
    echo "✅ Gemfile restored"
elif ! ruby -c Gemfile > /dev/null 2>&1; then
    echo "❌ CORRUPTION DETECTED: Invalid Ruby syntax"
    echo "🔧 Restoring from backup..."
    cp Gemfile.backup Gemfile
    echo "✅ Gemfile restored"
else
    echo "✅ Gemfile is clean"
fi

echo "📋 Current Gemfile status:"
head -5 Gemfile