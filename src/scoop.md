# Scoop

Is a package manager for Windows that allows you to install and manage software packages easily. It is designed to be simple and intuitive, making it easy for users of all skill levels to use.

## Installation

To install Scoop, open a PowerShell window as an administrator and run the following command:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

## Usage

Once Scoop is installed, you can use it to install and manage software packages. For example, to install Git, run the following command:

```powershell
scoop install git
```

Some packages are available in the default bucket, but you can also add additional buckets to install more packages. To add a bucket, run the following command:

```powershell
scoop bucket add [extras](bucket name here)
```

## Updating

To update Scoop and all installed buckets, run the following command:

```powershell
scoop update
```

To update the packages themselves, run the following command:

```powershell
scoop update -a
```

## Uninstalling

To uninstall Scoop, run the following command:

```powershell
scoop uninstall scoop
```
