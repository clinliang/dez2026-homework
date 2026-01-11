# Daily Git Workflow

## Typical Development Flow

1. Start from develop
```bash
git checkout develop
git pull
```

2. Create a branch
```bash
git checkout -b experiment/dbt-source-loader`
```

3. Work & commit regularly

4. Merge when done
```bash
git checkout develop
git merge experiment/dbt-source-loader`
```

5. Delete experiment branch
```bash
git branch -d experiment/dbt-source-loader
```

## Exploration Workflow
- exploration branches may live longer
- no pressure to merge
- merge only after cleanup and refactor

## Exercise Workflow
- work directly in exercise
- no merge, no cleanup required