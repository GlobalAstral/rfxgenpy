from __future__ import annotations
import ctypes
from enum import Enum
from random import randint
import wave
import struct

import rfxgenpy.rfxgen as rfxgen

class WaveType(Enum) :
  SQUARE = 0
  SAWTOOTH = 1
  SINE = 2
  NOISE = 3

class WaveParams :

  @staticmethod
  def fromRaw(raw: rfxgen.WaveParams) -> WaveParams : # type: ignore
    return WaveParams(
          pRandSeed=raw.randSeed, # type: ignore
          pWaveTypeValue=WaveType(raw.waveTypeValue), # type: ignore
          pAttackTime=raw.attackTimeValue, # type: ignore
          pSustainTime=raw.sustainTimeValue, # type: ignore
          pSustainPunch=raw.sustainPunchValue, # type: ignore 
          pDecayTime=raw.decayTimeValue, # type: ignore
          pStartFrequency=raw.startFrequencyValue, # type: ignore
          pMinFrequency=raw.minFrequencyValue, # type: ignore
          pSlide=raw.slideValue, # type: ignore
          pDeltaSlide=raw.deltaSlideValue, # type: ignore
          pVibratoDepth=raw.vibratoDepthValue, # type: ignore
          pVibratoSpeed=raw.vibratoSpeedValue, # type: ignore
          pChangeAmount=raw.changeAmountValue, # type: ignore
          pChangeSpeed=raw.changeSpeedValue, # type: ignore
          pSquareDuty=raw.squareDutyValue, # type: ignore
          pDutySweep=raw.dutySweepValue, # type: ignore
          pRepeatSpeed=raw.repeatSpeedValue, # type: ignore
          pPhaserOffset=raw.phaserOffsetValue, # type: ignore
          pPhaserSweep=raw.phaserSweepValue, # type: ignore
          pLpfCutoff=raw.lpfCutoffValue, # type: ignore
          pLpfCutoffSweep=raw.lpfCutoffSweepValue, # type: ignore
          pLpfResonance=raw.lpfResonanceValue, # type: ignore
          pHpfCutoff=raw.hpfCutoffValue, # type: ignore
          pHpfCutoffSweep=raw.hpfCutoffSweepValue # type: ignore
        )

  @staticmethod
  def load(filename: str) -> WaveParams :
    raw = rfxgen.LoadWaveParams(filename) # type: ignore
    return WaveParams.fromRaw(raw) # type: ignore

  def save(self, filename: str) :
    rfxgen.SaveWaveParams(self.params(), filename) # type: ignore
  
  def __init__(self,
               pRandSeed: int | None = None,
               pWaveTypeValue: WaveType = WaveType.SQUARE,
               pAttackTime: float = 0.0,
               pSustainTime: float = 0.30,
               pSustainPunch: float = 0.0,
               pDecayTime: float = 0.40,
               pStartFrequency: float = 0.30,
               pMinFrequency: float = 0.0,
               pSlide: float = 0.0,
               pDeltaSlide: float = 0.0,
               pVibratoDepth: float = 0.0,
               pVibratoSpeed: float = 0.0,
               pChangeAmount: float = 0.0,
               pChangeSpeed: float = 0.0,
               pSquareDuty: float = 0.0,
               pDutySweep: float = 0.0,
               pRepeatSpeed: float = 0.0,
               pPhaserOffset: float = 0.0,
               pPhaserSweep: float = 0.0,
               pLpfCutoff: float = 1.0,
               pLpfCutoffSweep: float = 0.0,
               pLpfResonance: float = 0.0,
               pHpfCutoff: float = 0.0,
               pHpfCutoffSweep: float = 0.0
              ) -> None:
    self.randSeed: int = pRandSeed if pRandSeed is not None else randint(0, 65534)
    self.waveTypeValue: WaveType = pWaveTypeValue 
    self.attackTime: float = pAttackTime 
    self.sustainTime: float = pSustainTime 
    self.sustainPunch: float = pSustainPunch 
    self.decayTime: float = pDecayTime 
    self.startFrequency: float = pStartFrequency 
    self.minFrequency: float = pMinFrequency 
    self.slide: float = pSlide 
    self.deltaSlide: float = pDeltaSlide 
    self.vibratoDepth: float = pVibratoDepth 
    self.vibratoSpeed: float = pVibratoSpeed 
    self.changeAmount: float = pChangeAmount 
    self.changeSpeed: float = pChangeSpeed 
    self.squareDuty: float = pSquareDuty 
    self.dutySweep: float = pDutySweep 
    self.repeatSpeed: float = pRepeatSpeed 
    self.phaserOffset: float = pPhaserOffset 
    self.phaserSweep: float = pPhaserSweep 
    self.lpfCutoff: float = pLpfCutoff 
    self.lpfCutoffSweep: float = pLpfCutoffSweep 
    self.lpfResonance: float = pLpfResonance 
    self.hpfCutoff: float = pHpfCutoff 
    self.hpfCutoffSweep: float = pHpfCutoffSweep 

    self.params = lambda : rfxgen.WaveParams(
      self.randSeed,
      self.waveTypeValue.value,
      self.attackTime,
      self.sustainTime,
      self.sustainPunch,
      self.decayTime,
      self.startFrequency,
      self.minFrequency,
      self.slide,
      self.deltaSlide,
      self.vibratoDepth,
      self.vibratoSpeed,
      self.changeAmount,
      self.changeSpeed,
      self.squareDuty,
      self.dutySweep,
      self.repeatSpeed,
      self.phaserOffset,
      self.phaserSweep,
      self.lpfCutoff,
      self.lpfCutoffSweep,
      self.lpfResonance,
      self.hpfCutoff,
      self.hpfCutoffSweep
    )

class Sound :
  @staticmethod
  def default() -> Sound:
    return Sound(WaveParams())

  @staticmethod
  def genPickupCoin() -> Sound :
    return Sound(WaveParams.fromRaw(rfxgen.GenPickupCoin())) # type: ignore
  
  @staticmethod
  def genLaserShoot() -> Sound :
    return Sound(WaveParams.fromRaw(rfxgen.GenLaserShoot())) # type: ignore
  
  @staticmethod
  def genExplosion() -> Sound :
    return Sound(WaveParams.fromRaw(rfxgen.GenExplosion())) # type: ignore
  
  @staticmethod
  def genPowerup() -> Sound :
    return Sound(WaveParams.fromRaw(rfxgen.GenPowerup())) # type: ignore
  
  @staticmethod
  def genHitHurt() -> Sound :
    return Sound(WaveParams.fromRaw(rfxgen.GenHitHurt())) # type: ignore
  
  @staticmethod
  def genJump() -> Sound :
    return Sound(WaveParams.fromRaw(rfxgen.GenJump())) # type: ignore
  
  @staticmethod
  def genBlipSelect() -> Sound :
    return Sound(WaveParams.fromRaw(rfxgen.GenBlipSelect())) # type: ignore
  
  @staticmethod
  def genRandomize() -> Sound :
    return Sound(WaveParams.fromRaw(rfxgen.GenRandomize())) # type: ignore

  def __init__(self, params: WaveParams) -> None:
    self.params = params

  def save(self, filename: str) :
    self.params.save(filename)

  def load(self, filename: str) :
    self.params = WaveParams.load(filename)

  def generate(self) -> list[float]:
    sample_count = ctypes.c_uint(0)
    raw = rfxgen.GenerateWave(self.params.params(), ctypes.byref(sample_count)) # type: ignore
    if not raw:
      raise MemoryError("GenerateWave returned NULL")
    
    try:
        samples: list[float] = [raw[i] for i in range(sample_count.value)]
        return samples
    finally:
      rfxgen.RFXGenFree(raw) # type: ignore

  def saveWav(self, filename: str, sampleRate: int = 44100) :
    samples = self.generate()

    with wave.open(filename, 'wb') as wav :
      wav.setnchannels(1)
      wav.setsampwidth(2) # 16 bit
      wav.setframerate(sampleRate)

      data = bytearray()

      for sample in samples :
        value = max(-1.0, min(1.0, sample))
        data.extend(struct.pack('<h', int(value * 32767)))

      wav.writeframes(data)
      wav.close()
