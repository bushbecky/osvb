# Python Data Model for OSVR extended xUnit files

from typing import Dict, List, Union, Optional
from pathlib import Path
from dataclasses import dataclass
from yamldataclassconfig.config import YamlDataClassConfig


@dataclass
class ImplementationMetadata(YamlDataClassConfig):
    """
    """


@dataclass
class RequirementsMetadata(YamlDataClassConfig):
    """
    """


@dataclass
class LogentryLocation(YamlDataClassConfig):
    """
    """
    Filename: str = None
    LineNumber: Optional[int] = None
    Offset: Optional[int] = None


@dataclass
class Logentry(YamlDataClassConfig):
    """
    """
    Time: str = None
    Severity: str = None
    Code: Optional[str] = None
    Message: str = None
    Location: Optional[LogentryLocation] = None


@dataclass
class Testcase(YamlDataClassConfig):
    """
    """
    Name: str = None
    Duration: Optional[float] = None
    Result: Optional[List[str]] = None
    Categories: Optional[List[str]] = None
    Metadata: Optional[Union[ImplementationMetadata, RequirementsMetadata]] = None
    Log: Optional[List[Union[str, Logentry]]] = None
    #Log: Optional[List[Logentry]] = None


@dataclass
class TestsuiteStats(YamlDataClassConfig):
    """
    """
    NumberOfTests: int = None
    Errors: int = None
    Failures: int = None
    Skipped: int = None


@dataclass
class Testsuite(YamlDataClassConfig):
    """
    """
    Tests: List[Testcase] = None
    Stats: TestsuiteStats = None
    #Metadata


@dataclass
class OpenSourceVerificationReport(YamlDataClassConfig):
    """
    """
    OSVRVersion: int = None
    Tool: str = None
    Suites: Dict[str, Testsuite] = None


def LoadOSVRFile(
    OSVRFilePath
):
    """
    Load an OSVR "extended xUnit" file in YAML format and unmarshal it.

    :param OSVRFilePath: location of the ``*.osvr.yml`` file to be loaded.
    """
    _cpath = Path(OSVRFilePath)
    _osvr = OpenSourceVerificationReport()
    _osvr.load(_cpath)
    _osvr.FILE_PATH = _cpath
    print(_osvr.FILE_PATH)
    print('OSVRVersion:', _osvr.OSVRVersion)
    print('Tool:', _osvr.Tool)
    for name, suite in _osvr.Suites.items():
        print('·', name)
        for test in suite.Tests:
            print()
            print(' -', test.Name)
            for item in test.Log:
                print(item)
            print()

    return _osvr
