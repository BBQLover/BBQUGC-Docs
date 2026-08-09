©︎ BBQ大好き All Rights Reserved.
<!-- source-revision: 1 -->

# Metadata and resources

Select the project, choose **Edit Metadata**, and complete the creator-facing fields. Closing the window saves your changes.

| Field | Guidance |
|---|---|
| `Id` | Tool-created identity. Preserve it for updates. |
| `Name` | Project and package name. Keep it stable. |
| `Version` | Numeric release value used for dependency selection. |
| `VersionName` | Human-readable version such as `1.0.0`. |
| `FriendlyName` | Display name shown to users. |
| `Description` | Short package summary. |
| `Category` | Best matching user-facing group, or `Other`. |
| `CreatedBy` | Creator or team display name. |
| URL fields | Public HTTPS links, or empty. |

For a normal update, keep the same project, `Id`, and `Name`. Create a new identity only for an intentionally incompatible replacement.

## Presentation resources

Place presentation files in `<ProjectRoot>/BBQ/Resources/`:

- `Cover.png`: square cover; 500×500 is a useful working size.
- `Description.png`: wide image; 1920×1080 is a useful working size.

The builder copies the complete physical resource tree. Avoid symbolic links and keep image sizes reasonable. Verify the copied files in the final package.
